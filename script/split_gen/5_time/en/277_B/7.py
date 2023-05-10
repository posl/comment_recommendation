def problem277_b():
    n = int(input())
    s = [input() for i in range(n)]
    print("Yes" if len(set(s)) == n else "No")
