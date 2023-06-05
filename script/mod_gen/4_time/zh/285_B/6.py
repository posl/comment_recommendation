def solve():
    n = int(input())
    s = input()
    for i in range(1, n):
        for j in range(n-i):
            if s[j] == s[j+i]:
                print(i)
                break
        else:
            print(n-i)
solve()
