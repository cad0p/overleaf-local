# overleaf-local

A local version of Overleaf, running on Docker. One click setup.

## Installation

### Requirements

- VS Code
- Docker

### Setup

1. Fork this repo
2. Open the repo in VS Code
3. Click on the green button at the bottom left corner of the window
4. Select `Reopen in Container`
5. Wait for the container to build (this may take a while)

### Projects setup

Projects will go in the top level of this repo. I recommend you to fork this repo and use that fork as your own Overleaf. You can then rebase your fork on this repo to get updates.

You can then run `git init` to initialize a git repo in each project folder, so that you can then push it to the project repo in GitHub or GitLab.
You can also commit changes directly in this repo (but I don't recommend it).

## Usage

Open <https://localhost:5050> after having opened this Dev Container (and waited for at least ~1min).

To save your Project(s) to this repo, every time you want to save and commit, run `./scripts/save` from the workspace folder (the one that opens by default when you open the terminal).

Run instead `zip -r YOUR_TITLE.zip YOUR_TITLE` (which can be shortened to `zip -r YOUR_TITLE{.zip,}`) to load it into Overleaf.

## Customization

You can customize the [`Dockerfile`](.devcontainer/Dockerfile) to choose if you want to install the full TeXLive distribution or just the basic one. You can also add your own packages.

I have added some examples of modifications commented out in the [`Dockerfile`](.devcontainer/Dockerfile).

## Disclaimer

This works best on x86-64 CPUs. If you have an ARM CPU, you may want to change the `FROM` line in the [`Dockerfile`](.devcontainer/Dockerfile). Feel free to open a PR if you know how to make it work natively on ARM CPUs.

## Acknowledgements

This project is based on Overleaf Toolkit ([quick start guide](https://github.com/overleaf/toolkit/blob/master/doc/quick-start-guide.md)), which is a part of [Overleaf](https://www.overleaf.com/).
