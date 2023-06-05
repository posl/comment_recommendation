def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    while True:
        flag = True
        for i in range(n):
            if a[i] % 2 == 1:
                flag = False
                break
            a[i] //= 2
        if flag:
            ans += 1
        else:
            break
    print(ans)
