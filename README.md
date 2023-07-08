# overleaf-local

A local version of Overleaf, running on Docker. One click setup.

## Installation

### Requirements

- VS Code
- Docker

## Usage

Open <https://localhost:5050> after having opened this Dev Container (and waited for at least ~1min)

To save your Project(s) to this repo, every time you want to save and commit, run `./scripts/save` from the workspace folder (the one that opens by default when you open the terminal).

Run instead `zip -r YOUR_TITLE.zip YOUR_TITLE` (which can be shortened to `zip -r YOUR_TITLE{.zip,}`) to load it into Overleaf.

## Acknowledgements

This project is based on Overleaf Toolkit ([quick start guide](https://github.com/overleaf/toolkit/blob/master/doc/quick-start-guide.md)), which is a part of [Overleaf](https://www.overleaf.com/).
