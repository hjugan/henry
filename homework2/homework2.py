# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
#Git runs on your computer to track local changes to code in the staging area. GitHub is a website that stores coding projects. Git Bash allows window users to use git commands.

# 2) What’s the difference between the terminal and the command line?
# The terminal is the software that allows you to communicate with the computer. The command line is the literal interface in terminal where you give commands and read the computers responses

# 3) How does Windows PowerShell differ from Git Bash?
#Windows powershell runs natively on windows while git bash is a shell that you must install and run separetly. Gitbash is text based and WPS is object oriented

# 4) What’s the difference between Anaconda, conda, and Python?
#Python is a programming language, Anaconda is a "more complete" version of python that allows you to access and use tons of tools and libraries that are specialized and helpful for additional tasks.
#Conda is a tool that is included with Anaconda, it is a package and environment manager which means it helps you keep your projects organized and running smoothly, even if they have multiple dependencies or languages.

# 5) What is VS Code? 
#VS Code is a code development interface that allows you to edit and run code, with tons of ease-of-access features

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
#Jupyter Notebook is a website that allows you to create and share documents containing code
#Jupyter Lab is more like VS Code where it has a ton of features that allow you to do mroe with the code. 

# 7) What does ~/ mean?
#Home directory

# 8) What’s the difference between an absolute path and a relative path?
#An absolute path gives the directory from the home directory while a relative path gives the directory to a file from the current working directory

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
#Users/hjugan/Desktop/School/2025/Fall/ASTRO\ 98/Python_DeCal_fa25/course_assignments/homework2/
#../../course_assignments/homework2/

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# cd ..

# 11) What would rm ./ do in your current directory? (Don’t try it!)
# remove the file from the computer

# 12) What do the following commands do?
# git add -> adds code to the staging area where it can be edited and have changes monitored
# git commit -> saves changes to the code locally
# git push -> saves the changes to the code remotely and adds it to github

# 13) What's the difference between "git add ." and "git add <file>"?
# git add . will add the current directory to the staging area while git add <file> adds the file

# 14) What do "git status" and "git log -1" do?
#git status gives you a ton of information about the project you are currently editing, including the working directory, the changes to be committed/not commited, and files that are not in the staging area that have been created
# git log -1 shows you the most recent commit to your git history so you dont have to scroll through your entire commit history

# 15) What’s the difference between cloning a repository and pulling from it?
# Git clone clones an entire repository, and it is useful if you do not have the repository at all on your computer
#git pull essentially updates a repository you have already cloned, giving your version of a repository the latest version on github

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
#I was using the mv command to move a file to a different directory, but I forgot the / after the directory so it renamed my file and I couldnt figure out where the file went lol

# 17) What’s a question you still have? What’s something you’re confused about?
#I dont have any specific questions yet but I want to keep working with git because there are some parts of the process that are unfamiliar to me still

# 18) Tell me a fun fact!
#Light can be considered a particle or a wave depending on the circumstance in which you view it!

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)

x = 3j
y = 4j
print(x*y)
#This expression may look simple, but it is actually complex (ba-dum-tss). It multiplies two complex numbers together and returns a real number doing
#imaginary arithmatic in the process (the imaginary components become real)