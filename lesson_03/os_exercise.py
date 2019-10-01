'''
Exercise
# 1. create a folder and name the folder 'os_exercises.'
# 2. In that folder create a file. Name the file 'exercise.py'
# 3. get input from the console and write it to the file.
# 4. repeat step 2 and 3 (name the file something else).
# 5. read the content of the files and print to console the content of the file with the largest amount of unique words.
'''

import os
import errno
import subprocess
try:
    os.mkdir("os_exercises")
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass


command = input('Type "create" or "read"\n') + ''
if command == "quit":
    quit()
if command == 'create':
    new_file_name = input("Type in a new filename: \n" + '')
    path = "os_exercises/" + new_file_name
    content = input("Type what content the file should have: \n" + '')
    with open(path, 'w') as file_object:
        file_object.write(content)
if command == 'read':
    # print("Here is the content from the file with the most unique words:")
    # Save a list with all existing files
    path = 'D:\\Coding\\python_elective\\Lesson-03-Utillities-modules-Virtual-Enviroment\\exercises\\os_exercises'
    files = []
    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.py' in file:
                files.append(os.path.join(r, file))
    print(files)
    # Look through files to see which has the most unique words
    file_content_list = []
    file_content_set = {}
    for file in files:
        with open(file, "r") as word_list:
            file_content_list = word_list.read().split(' ')
        file_content_set = set(file_content_list)
        print('The unique words in ' + file + ': ', end='')
        print(file_content_set)