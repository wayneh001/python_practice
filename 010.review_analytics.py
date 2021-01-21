data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
    	data.append(line)
    	count += 1
    	if count % 1000 == 0:
    	    print(len(data))
print()
print('Total', len(data), 'reviews read.')
print()

sum_len = 0
for d in data:
    sum_len += len(d)
    avg = sum_len / len(data)
print('Average lenth of reviews is', avg, '.')
print()

len_select = []
for d in data:
    if len(d) < 100:
    	len_select.append(d)
print('Total', len(len_select), 'reviews are less than 100 words.')
print()
print('The first review that less than 100 words is:\n', len_select[0])

good_select = []
for d in data:
    if 'good' in d:
    	good_select.append(d)
print('Total', len(good_select), 'reviews mentioned "good" in reviews.')
print()
print('The first review that mentioned "good" is:\n', good_select[0])

# 另解
# good_select = [d for d in data if 'good' in d]
# bad_select = ['bad' in d for d in data]