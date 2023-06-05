def check_seven(n):
    if '7' in str(n):
        return True
    else:
        return False
N = int(input())
count = 0
for i in range(1,N+1):
    if check_seven(i):
        continue
    else:
        if check_seven(oct(i)):
            continue
        else:
            count += 1
print(count)

if __name__ == '__main__':
    check_seven()