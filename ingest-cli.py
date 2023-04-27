import argparse
from pathlib import Path
from ingest2 import ingest

parser = argparse.ArgumentParser()

parser.add_argument("source")
parser.add_argument("target")

args = parser.parse_args()

source = Path(args.source)
target_dir = Path(args.target)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

if not source.exists():
    print("The source doesn't exist")
    raise SystemExit(1)

ingest(source, target_dir)
# print("ingested corpus from " + source + " into db in " + target_dir)
