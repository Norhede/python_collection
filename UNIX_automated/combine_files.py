def combine_files(first_file, second_file, target_file):
    first_list = []
    second_list = []
    file_object = open(first_file)
    for line in file_object:
        string = line.replace("\n", "")
        first_list.append(string)
    file_object.close()
    file_object2 = open(second_file)
    for line in file_object2:
        second_list.append(line)
    file_object2.close()
    combined_list = [str(first_list[i]) + str(second_list[i]) for i in range(len(first_list))]
    # print(combined_list)   # Prints to confirm list contents
    with open(target_file, 'w') as file_object3:
        for item in combined_list:
            file_object3.write(item)


def print_file(file):
    file_object = open(file)
    for line in file_object:
        print(line)


combine_files("file1.txt", "file2.txt", "file3.txt")
print_file("file3.txt")
