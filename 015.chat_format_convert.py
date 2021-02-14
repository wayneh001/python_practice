def read_file(filename):
    chat_list = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            chat_list.append(line.strip())
    return chat_list
    

def convert(chat_list):
    convert_list = []
    name = None
    for line in chat_list:
        if line == 'Albert':
            name = 'Albert'
            continue
        elif line == 'Mr. Liu':
            name = 'Mr.Liu'
            continue
        if name:
            convert_list.append(name + ': ' + line)
    return convert_list

def write_file(file_name, chat_list):
    with open(file_name, 'w', encoding = 'utf-8') as f:
        for chat in chat_list:
    	    f.write(chat + '\n')
        

def main():
    chat_list = read_file('input.txt')
    chat_list = convert(chat_list)
    write_file('output.txt', chat_list)

main()