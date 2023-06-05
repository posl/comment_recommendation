def judge(s):
    if s % 3 == 0 or s % 5 == 0:
        return True
    else:
        return False
n = int(input())
l = list(map(int, input().split()))
flag = True
for i in l:
    if i % 2 == 0:
        if judge(i) == False:
            flag = False
            break

if __name__ == '__main__':
    judge()