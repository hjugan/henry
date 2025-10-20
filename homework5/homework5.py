"""
git vs. GitHub: Git is the process that carries out git commands and github is an online repository that stores code

Terminal vs Command Line: The terminal is the application on your computer that allows you to use commands to carry out processes on your computer, the command line is the actual place that you enter the commands into

Local vs Remote Repository: A local repository exists on your computer and a rempote repository exists elsewhere

Version control: the task of having a software on your system up to date

Staging area: the staging area is the place on your computer where you can make changes to a local repository in github

git add: Stages changes in your files, marking them as ready to be included in the next "snapshot" or commit.

git commit: Saves the staged snapshot of your project's files to the local repository's history with a descriptive message.

git push: Uploads your locally committed changes to a remote repository (like GitHub), sharing them with your team.

git status: Shows you which files have been modified, which are staged, and which are untracked in your current working directory.

git pull: Fetches the latest changes from a remote repository and automatically merges them into your current local branch.

pwd: Displays the full, absolute path of the directory you are currently in.

ls: Lists all the files and folders contained within your current directory.

cd: Allows you to navigate from your current directory to a different specified directory.

nano: Opens a simple, beginner-friendly text editor directly inside your terminal to create or edit files.

touch: Creates a new, empty file with the specified name or, if the file already exists, updates its access and modification timestamps.

mv: Moves a file or directory from one location to another, or renames a file or directory if the destination is in the same location.

rm: Permanently deletes one or more specified files or directories from your system.

cat: Reads one or more files and prints their entire contents to the terminal screen.
"""

"""
pwd
ls
cd ../brianna_repo
git pull origin main
cp homework.py ../judy_decal/homework
cd ../judy_decal/homework
ls
git add .
git add homework.py
git commit -m "homework is done"
Judy didn't pull the latest version of the repository before trying to update it.
users/judy/recent
"""

def get_data_type(data_input):
    type_name = type(data_input).__name__
    return f"The data type is: {type_name}"

def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"    

def sum_list_with_loop(numbers_list):
    total_sum = 0
    for number in numbers_list:
        total_sum += number
    return total_sum

def duplicate_elements(input_list):
    duplicated_list = []
    for item in input_list:
        duplicated_list.append(item)
        duplicated_list.append(item)
    return duplicated_list

#The code does not have a bug in it, it works fine.

list = [10, 125, 43, 93, 0, 44]
print(duplicate_elements(list))