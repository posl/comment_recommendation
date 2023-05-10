def problem277_b():
    n = int(input())
    s = [input() for i in range(n)]
    print("Yes" if len(set(s)) == n else "No")

if __name__ == '__main__':
    problem277_b()