data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
    	data.append(line)
    	count += 1
    	if count % 1000 == 0:
    	    print(len(data))
print('Total', len(data), 'reviews read.')

sum_len = 0
for d in data:
    sum_len += len(d)
    avg = sum_len / len(data)
print('Average lenth of reviews is', avg, '.')

len_select = []
for d in data:
    if len(d) < 100:
    	len_select.append(d)
print('Total', len(len_select), 'reviews are less than 100 words.')
print(len_select[0])