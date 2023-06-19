def main():
    #n = int(input())
    #s = list(map(int, input().split()))
    n = 5
    s = [666,777,888,777,666]
    ans = 0
    for i in range(n):
        if s[i] % 2 == 0:
            ans += 1
        if s[i] % 3 == 2:
            ans += 1
    print(ans)
