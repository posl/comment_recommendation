def main():
    n = int(input())
    a = list(map(int, input().split()))
    flag = True
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                flag = False
                break
    if flag:
        print('APPROVED')
    else:
        print('DENIED')
