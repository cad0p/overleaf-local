#!/usr/bin/bash
# run from the default workspace folder
mkdir -p tmp
docker exec mongo bash -c "mongoexport --db=sharelatex --collection='projects' --jsonArray --out=files.json"
docker exec mongo bash -c "mongoexport --db=sharelatex --collection='docs' --jsonArray --out=docs.json"
docker exec mongo bash -c "mongoexport --db=sharelatex --collection='users' --jsonArray --out=users.json"
docker cp mongo:/files.json tmp/
docker cp mongo:/docs.json tmp/
docker cp mongo:/users.json tmp/
python3 scripts/analyze.py
