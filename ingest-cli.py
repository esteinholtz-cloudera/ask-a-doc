import argparse, os
from pathlib import Path
from ingest2 import ingest

parser = argparse.ArgumentParser()

parser.add_argument("source")

args = parser.parse_args()

source = Path(args.source)
target_dir = Path(os.getenv('DBPATH'))

if not source.exists():
    print("The source doesn't exist")
    raise SystemExit(1)

ingest(source, target_dir)
# print("ingested corpus from " + source + " into db in " + target_dir)
