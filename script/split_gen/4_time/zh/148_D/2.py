def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    if n == 1:
        print(0)
        return
    if a[0] != 1:
        print(-1)
        return
    a.append(0)
    a.append(0)
    #print(a)
    ans = 0
    for i in range(n):
        if a[i+1] == a[i] + 1:
            ans += 1
        elif a[i+1] > a[i] + 1:
            print(-1)
            return
    print(n - ans)
