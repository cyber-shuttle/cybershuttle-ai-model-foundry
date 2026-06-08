"""
Foundry schema definitions.

These Pydantic models are the authoritative source of truth for all registry
objects. JSON Schema files in schemas/ are generated from them — never edit
those files directly.

Usage:
    python tools/generate_schemas.py
"""

from __future__ import annotations

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Shared enums
# ---------------------------------------------------------------------------

class LifecycleStatus(str, Enum):
    candidate = "candidate"
    registered = "registered"
    containerized = "containerized"
    nexus_tested = "nexus-tested"
    benchmarked = "benchmarked"
    optimized = "optimized"
    cybershuttle_ready = "cybershuttle-ready"
    production = "production"


class NexusValidation(str, Enum):
    untested = "untested"
    in_progress = "in-progress"
    passed = "passed"
    failed = "failed"


class BenchmarkStatus(str, Enum):
    not_started = "not-started"
    in_progress = "in-progress"
    complete = "complete"


class OptimizationStatus(str, Enum):
    not_started = "not-started"
    in_progress = "in-progress"
    complete = "complete"


class WorkflowStatus(str, Enum):
    candidate = "candidate"
    draft = "draft"
    validated = "validated"
    production = "production"


class TaskType(str, Enum):
    inference = "inference"
    fine_tuning = "fine-tuning"
    training = "training"
    evaluation = "evaluation"
    deployment = "deployment"
    benchmarking = "benchmarking"


# ---------------------------------------------------------------------------
# model.schema.json
# ---------------------------------------------------------------------------

class UpstreamSources(BaseModel):
    huggingface: Optional[str] = Field(None, description="HuggingFace model ID, e.g. ibm/MoLFormer-XL-both-10pct")
    github: Optional[str] = Field(None, description="GitHub repository URL")
    paper: Optional[str] = Field(None, description="arXiv or DOI URL for the primary paper")
    ngc: Optional[str] = Field(None, description="NVIDIA NGC model URL")
    bionemo: Optional[str] = Field(None, description="BioNeMo Framework model reference")
    other: Optional[list[str]] = Field(None, description="Any other upstream references")


class LifecycleConfig(BaseModel):
    supported_stages: list[TaskType] = Field(
        description="Task types this model supports"
    )


class DatasetRef(BaseModel):
    recommended: Optional[list[str]] = Field(None, description="Recommended dataset IDs")
    supported: Optional[list[str]] = Field(None, description="Known-compatible dataset IDs")


class ReadinessStatus(BaseModel):
    registry_status: LifecycleStatus = Field(
        default=LifecycleStatus.candidate,
        description="Current lifecycle stage"
    )
    nexus_validation: NexusValidation = Field(
        default=NexusValidation.untested
    )
    benchmark_status: BenchmarkStatus = Field(
        default=BenchmarkStatus.not_started
    )
    optimization_status: OptimizationStatus = Field(
        default=OptimizationStatus.not_started
    )
    workflow_status: WorkflowStatus = Field(
        default=WorkflowStatus.candidate
    )


class CybershuttleConfig(BaseModel):
    enabled: bool = Field(default=False)
    workflow_templates: Optional[list[str]] = Field(None)


class MaintainerEntry(BaseModel):
    name: str
    github: str
    affiliation: Optional[str] = None


class ModelSchema(BaseModel):
    """
    Schema for registry/models/<domain>/<model-id>/model.yaml
    """
    schema_version: str = Field(
        default="1.0",
        alias="$schema_version",
        description="Schema version, not the $schema header (that is added by YAML tooling)"
    )
    id: str = Field(description="Unique model identifier, lowercase, hyphen-separated")
    name: str = Field(description="Human-readable model name")
    description: Optional[str] = Field(None, description="Short description (1-2 sentences)")
    domain: list[str] = Field(description="Scientific domain(s)")
    model_family: list[str] = Field(description="Model architecture / family tags")
    tasks: list[TaskType] = Field(description="Supported task types")
    upstream: UpstreamSources
    lifecycle: LifecycleConfig
    datasets: Optional[DatasetRef] = None
    resource_profiles: Optional[dict[str, list[str]]] = Field(
        None,
        description="Keys: recommended, supported. Values: paths to resource profile YAML files."
    )
    optimization_profiles: Optional[dict[str, list[str]]] = Field(
        None,
        description="Keys: recommended, supported. Values: paths to optimization profile YAML files."
    )
    cybershuttle: Optional[CybershuttleConfig] = None
    readiness: ReadinessStatus = Field(default_factory=ReadinessStatus)
    maintainers: Optional[list[MaintainerEntry]] = None
    notes: Optional[str] = None

    model_config = {"populate_by_name": True}


# ---------------------------------------------------------------------------
# resource_profile.schema.json
# ---------------------------------------------------------------------------

class GPUSpec(BaseModel):
    model: str = Field(description="GPU model, e.g. NVIDIA B200, NVIDIA RTX 6000 Ada")
    count: int = Field(ge=1)
    vram_gb: float = Field(ge=0, description="VRAM per GPU in GB")
    interconnect: Optional[str] = Field(None, description="e.g. NVLink, PCIe")


class CPUSpec(BaseModel):
    cores: Optional[int] = None
    ram_gb: Optional[float] = None


class StorageSpec(BaseModel):
    local_ssd_gb: Optional[float] = None
    scratch_gb: Optional[float] = None
    parallel_fs: Optional[str] = Field(None, description="e.g. GPFS, Lustre, NFS")


class ResourceProfileSchema(BaseModel):
    """
    Schema for resource-profiles/<system>/<profile-id>.yaml
    """
    id: str
    name: str
    system: str = Field(description="System name, e.g. nexus, google-tpu, access-delta")
    partition: Optional[str] = Field(None, description="HPC partition or queue name")
    gpu: Optional[GPUSpec] = None
    cpu: Optional[CPUSpec] = None
    storage: Optional[StorageSpec] = None
    max_walltime_hours: Optional[float] = None
    scheduler: Optional[str] = Field(None, description="e.g. slurm, pbs, kubernetes")
    notes: Optional[str] = None
