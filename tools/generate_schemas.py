#!/usr/bin/env python3
"""
Generate JSON Schema files from Pydantic model definitions.

Run after any change to tools/schemas/schemas.py:
    python tools/generate_schemas.py

Output goes to schemas/. Never edit those files by hand.
"""

import json
from pathlib import Path

from tools.schemas.schemas import ModelSchema, ResourceProfileSchema

SCHEMA_DIR = Path("schemas")
SCHEMA_DIR.mkdir(exist_ok=True)

MODELS = [
    (ModelSchema, "model.schema.json"),
    (ResourceProfileSchema, "resource_profile.schema.json"),
]

for model_cls, filename in MODELS:
    schema = model_cls.model_json_schema()
    # Add $schema declaration for JSON Schema 2020-12
    schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    out = SCHEMA_DIR / filename
    out.write_text(json.dumps(schema, indent=2) + "\n")
    print(f"  wrote {out}")

print("Done.")
