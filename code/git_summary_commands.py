# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:26:31 2020

@author: eyasari
"""


import numpy as np
#%%
https://about.gitlab.com/images/press/git-cheat-sheet.pdf
https://rogerdudler.github.io/git-guide/
https://book.git-scm.com/book/en/v2

Check you git setting:
	- git config --list 

View your git settings and where they come from:
	- git config --list --show-origi 

git config --global user.name "John Doe"
git config --global user.email johndoe@example.com 


To Create new repository:
	- Git init

To clone:

	- git clone link_to_the_repository


To Pull:

	- git pull origin master
Or
	- git pull origin name_of_the_branch

To Create a new branch:
	- git checkout -b new-branch_name
	
	
To Delete the branch:
	- git branch -d feature_x

To add new file to stage level:
To Track new files:
To marke merging-conflicts files as resolved
It may be helpful to think of it more as “add precisely this content to the next commit" 

	- git add filepath/name_here

By doing the add command, we put the files in the stageing area which allows us to do commits


To save our changes in the code we need to commit:
	- git commit -m 'descriptive message here'

To push our commit to the remote repository:
	- git push orging master
	- git push origin branch_name

To restore the staged (to unstage):
	- git restore --staged <file> 

git restore <file> to discard changes in working directory

To replace local changes if you did something wrong:
	- git checkout --<filename>
This will replace the changes in your working tree with the last content in HEAD


Combine stage and commit together:
Adding the -a option to the git commit command makes
Git automatically stage every file that is already tracked before doing the commit, letting you skip
the git add part: 
