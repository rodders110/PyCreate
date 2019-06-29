#!/usr/bin/env python

import os, git, requests, json, sys

f = open('Config.txt', 'r')
data = f.readlines()
homeDir = data[0].rstrip()
user = data[1].rstrip()
token = data[2].rstrip()
f.close()
dirName = sys.argv[1]
payload = {'name': dirName, 'auto_init': 'true'}

def createDir():
    path = f'{homeDir}{dirName}'
    print(path)
    try:
        os.mkdir(path)
        print(f'Directory {dirName} created')
    except FileExistsError:
        print(f'Directory {dirName} already exists')

def createReadMe():
    path = homeDir + "readme.txt"
    f = open(path, 'w+')
    print('readme file created')
    f.close()

def createGitRepo():
    requests.post('https://api.github.com/' + 'user/repos', auth=(user,token), data=json.dumps(payload))

def gitInitCommit():
    path = homeDir + dirName
    r = git.Repo.init(path)
    r.index.add('*')
    r.index.commit('first commit')

    remote = r.create_remote(dirName, url = f'https://github.com/{user}/{dirName}.git')
    remote.push(refspec='master:master')
    r.close()

    

def main():
    createDir()
    createReadMe()
    print('Creating Github Repo...')
    createGitRepo()
    print('Initialise Git and push to master....')
    gitInitCommit()
    print('Done!')
    

    


if __name__ == "__main__":
    main()
