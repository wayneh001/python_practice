data = []
count = 0
with open('010.reviews.txt', 'r') as f:
    for line in f:
    	data.append(line)
    	count += 1
    	if count % 1000 == 0:
    	    print(len(data))
print()
print('Total', len(data), 'reviews read.')
print()

words_count = {}
for d in data:
    words = d.split()
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

print('Total', len(words_count), 'words in review.')
for word in words_count:
    if words_count[word] > 10000:
            print(word, words_count[word])
    
while True:
    word = input('Enter a word to count.')
    if word == 'q':
        break
    if word in words_count:
        print('Total', words_count[word], 'times in review.')
    else:
        print('Not in review.')
print('Thanks for use.')