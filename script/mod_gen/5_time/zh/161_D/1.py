def check(n):
    n = str(n)
    for i in range(len(n)-1):
        if abs(int(n[i])-int(n[i+1]))>1:
            return False
    return True
k = int(input())
n = 0
while True:
    if check(n):
        k -= 1
    if k == 0:
        print(n)
        break
    n += 1

if __name__ == '__main__':
    check()