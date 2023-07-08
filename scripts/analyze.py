#!/usr/bin/python3

import json
from pathlib import Path
import shutil

# your sharelatex data folder
sharelatex_data = "/var/lib/sharelatex"
refs_folder = f"{sharelatex_data}/data/user_files/"


def copy(addr_type, path, oid, pid, owner):
    mypath = "./" + path
    if addr_type == "folders":
        Path(mypath).mkdir(parents=True, exist_ok=True)
    if addr_type == "fileRefs":
        shutil.copyfile(refs_folder + f"{pid}_{oid}", mypath)
    if addr_type == "docs":
        with open(mypath, "w") as f:
            f.write(raw_docs[oid])


def parse(obj, root="", project_id="", project_name="", owner=""):
    oname = obj["name"]
    if oname == "rootFolder":
        oname = project_name
    copy("folders", root + "/" + oname, obj["_id"]["$oid"], project_id, owner)

    if "folders" in obj:
        for folder in obj["folders"]:
            oname = obj["name"]
            if oname == "rootFolder":
                oname = project_name
            parse(
                folder,
                root=root + "/" + oname,
                project_id=project_id,
                project_name=project_name,
                owner=owner,
            )

    if "docs" in obj:
        for doc in obj["docs"]:
            oname = obj["name"]
            if oname == "rootFolder":
                oname = project_name
            copy(
                "docs",
                root + "/" + oname + "/" + doc["name"],
                doc["_id"]["$oid"],
                project_id,
                owner,
            )

    if "fileRefs" in obj:
        for fref in obj["fileRefs"]:
            oname = obj["name"]
            if oname == "rootFolder":
                oname = project_name
            copy(
                "fileRefs",
                root + "/" + oname + "/" + fref["name"],
                fref["_id"]["$oid"],
                project_id,
                owner,
            )


raw_docs = {}
with open("./tmp/docs.json") as json_file:
    docs = json.load(json_file)
    for doc in docs:
        raw_docs[doc["_id"]["$oid"]] = "\n".join(doc["lines"])

with open("./tmp/files.json") as json_file:
    obj = json.load(json_file)

users = {}

with open("./tmp/users.json") as json_file:
    uobj = json.load(json_file)
    for user in uobj:
        users[user["_id"]["$oid"]] = {
            "email": user["email"],
            "first_name": user["first_name"],
        }


for project in obj:
    print("----")
    print(project["name"], project["_id"]["$oid"])
    parse(
        project["rootFolder"][0],
        project_id=project["_id"]["$oid"],
        project_name=project["name"],
        owner=project["owner_ref"]["$oid"],
    )
