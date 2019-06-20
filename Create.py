#!/usr/bin/env python3

import os
import git




homeDir = '/home/roddy/Documents/Python/'
dirName = f'{homeDir}newProject'



def nameDir():
    try:
        os.makedirs(dirName)
        print(f'Directory {dirName} created')
    except FileExistsError:
        print(f'Directory {dirName} already exists')

def createReadMe():
    f = open(f'{dirName}/readme.md', 'w+')
    print('readme file created')
    f.close()

def gitInit():
    r = git.Repo.init(dirName)
    r.index.add('*')
    r.index.commit('first commit')
    remote = r.create_remote('newProject', url='https://github.com/rodders110/newProject.git')
    remote.push(refspec='master:master')
    r.close()
    

def main():
    nameDir()
    createReadMe()
    gitInit()

    

    


if __name__ == "__main__":
    main()