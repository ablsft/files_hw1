import os

def path_to_file(file_name):
    current_folder = os.getcwd()
    return os.path.join(current_folder, file_name)

def file_to_list(file_name):
    converted = []
    with open(path_to_file(file_name), encoding='utf-8') as text:
        for string in text:
            converted.append(string)  

    return converted

def files_to_dict(file_names):
    files_dict = {}
    for file in file_names:
        text = file_to_list(file)
        files_dict[len(text)] = [file, text]

    return files_dict

file_names = ['1.txt', '2.txt', '3.txt']

with open('output.txt', 'w', encoding='utf-8') as output:
    for item in sorted(files_to_dict(file_names).items()):
        output.write(item[1][0] + '\n')
        output.write(str(item[0]) + '\n')
        output.write(''.join(item[1][1]) + '\n')


