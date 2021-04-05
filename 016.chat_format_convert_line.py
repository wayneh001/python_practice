def read_file(filename):
    chat_list = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            chat_list.append(line.strip())
    return chat_list
    

def convert(chat_list):
    tina_words_count = 0
    tina_sticker_count = 0
    tina_image_count = 0
    wayne_words_count = 0
    wayne_sticker_count = 0
    wayne_image_count = 0
    for line in chat_list:
        split_list = line.split(' ')
        name = split_list[1]
        if name == 'Tina':
            if split_list[2] == 'Sticker':
                tina_sticker_count += 1
            elif split_list[2] == 'Image':
                tina_image_count += 1
            else:
                for message in split_list[2:]:
                    tina_words_count += len(message)
        elif name == 'Wayne':
            if split_list[2] == 'Sticker':
                wayne_sticker_count += 1
            elif split_list[2] == 'Image':
                wayne_image_count += 1
            else:
                for message in split_list[2:]:
                    wayne_words_count += len(message)
    print('Tina says', tina_words_count, 'words,', tina_sticker_count, 'stickers and', tina_image_count, 'images.')
    print('Wayne says', wayne_words_count, 'words,', wayne_sticker_count, 'stickers and',  wayne_image_count, 'images.')


def write_file(file_name, chat_list):
    with open(file_name, 'w', encoding = 'utf-8') as f:
        for chat in chat_list:
    	    f.write(chat + '\n')
        

def main():
    chat_list = read_file('016.[LINE] 與黃怡韶的聊天.input.txt')
    convert(chat_list)

main()

# time = s[0][:5]
# name = s[0][5:]