"""Validate an independent crate release tag; Python 3.11+."""
import os
from pathlib import Path
import tomllib


def verify():
    with Path("Cargo.toml").open("rb") as source:
        package = tomllib.load(source)["package"]
    tag = os.environ["RELEASE_TAG"]
    if tag != "v" + package["version"]:
        raise SystemExit(f"Tag {tag} must match crate version {package['version']}")
    return tag, package


if __name__ == "__main__":
    verify()
