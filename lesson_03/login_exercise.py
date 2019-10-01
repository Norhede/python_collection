# Exercise:
#	* Create a login application, that can store and handle multiple users.
#	* The user should be asked if he wants to log in or create a login.
#	* If 'create': The users credentials should be written to a file
#	* If 'login': The users information should be checked agains the content of the file. 
#	* The user should be granted or denied acces. 
#
# Go for the simplest, easiest, fastest approach!
#
# Most of what you need we already have covered, the rest is easy.
# You get 15 min. 
# Then we do it together


import abc

list_of_logins = []
command = input('Type "create" or "login"\n') + ''
if command == 'create':
    username = input('Type username: \n') + ''
    password = input('Type password: \n') + ''
    with open("logins.txt", 'w') as file_object:
        file_object.write(username + "&" + password)
if command == 'login':
    username = input('Type username: \n') + ''
    password = input('Type password: \n') + ''
    file_object = open("logins.txt")
    for line in file_object:
        list_of_logins.append(line)
    for item in list_of_logins:
        if item == username + '&' + password:
            print("You're logged in, woohoo!")
            exit()
    print("I'm sorry, you couldn't login!")
