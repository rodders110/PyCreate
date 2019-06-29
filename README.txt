
This is a Python script that automates the creation of a new project folder, it will then create a new Repo on your github and then comit from your local repo to github for you.

Once dowloaded please create a Config.txt file in the same directory as Create.py with the following information, in this exact order and on separate lines:

1. Absolute path to directory to where you wish the your projects to be saved
2. Your github username
3. Personal Access Token - you can create these on Github Settings>
developer Settings>Personal access tokens


This script uses Python3.6. The following libraries need to be installed:

gitpython - to install using pip:
pip install gitpython

requests - to install using pip:
pip install requests

