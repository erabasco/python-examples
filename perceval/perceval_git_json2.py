#! /usr/bin/env python3
# Count commits
# You can execute this script following this tutorial:
# https://grimoirelab.gitbooks.io/training/perceval/first_steps.html
# source ~/venvs/perceval/bin/activate 
# $ python3 ~/git/python-examples/perceval/perceval_git_json.py https://github.com/grimoirelab/perceval.git /tmp/clonedir

import argparse

from perceval.backends.core.git import Git
from pprint import pprint
# Read command line arguments
parser = argparse.ArgumentParser(description = "Count commits in a git repo")
parser.add_argument("repo", help = "Repository url")
parser.add_argument("dir", help = "Directory for cloning the repository")
parser.add_argument("--print", action='store_true', help = "Print hashes")
args = parser.parse_args()

# create a Git object, and count commmits
repo = Git(uri=args.repo, gitpath=args.dir)
count = 0
commit_prev = ""
author_prev = ""
commit_cur = ""
author_cur = ""
for commit in repo.fetch():
    if (commit_prev == ""):
        commit_prev = commit['data']['commit']
    else:
        commit_prev = commit_cur
    if (author_prev == ""):
        author_prev = commit['data']['Author']
    else:
        author_prev = author_cur
    commit_cur = commit['data']['commit']
    author_cur = commit['data']['Author']
    print("\n")
    print(commit_prev + ": " + author_prev)
    print(commit_cur + ": " + author_cur)            
    print(commit['data']['commit'])
    if args.print:
        print(commit['data']['commit'])
    count += 1

print("\nNumber of commmits: %d." % (count))
