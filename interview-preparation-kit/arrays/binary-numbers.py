n = int(input())
bi_num = ""

while(n > 0):
    remainder = n % 2
    n = n//2
    bi_num = str(remainder) + bi_num

count_list = []
count = 0

for i in range(len(bi_num) - 1):
    if bi_num[i] == "1":
        count += 1
    else:
        count_list.append(count)
        count = 0

if bi_num[len(bi_num) - 1] == "1":
    count += 1
    count_list.append(count)
elif bi_num[len(bi_num) - 1] == "0":
    count_list.append(count)

max_repeat = max(count_list)
print(max_repeat)

