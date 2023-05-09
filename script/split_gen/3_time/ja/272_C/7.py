def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    ans = -1
    for i in range(n):
        if a[i]%2 == 0:
            ans = a[i]
            break
    print(ans)
