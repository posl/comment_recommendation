def check_num(num):
    num_str = str(num)
    for i in range(len(num_str)-1):
        if abs(int(num_str[i]) - int(num_str[i+1])) > 1:
            return False
    return True
k = int(input())
count = 0
num = 1
while True:
    if check_num(num):
        count += 1
    if count == k:
        print(num)
        break
    num += 1
