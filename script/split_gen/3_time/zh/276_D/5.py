def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        flag = True
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            elif a[i] % 3 == 0:
                a[i] = a[i] / 3
            else:
                flag = False
        if flag == False:
            break
        ans += 1
    print(ans)
