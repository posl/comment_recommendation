def problem126_a():
    n,k = map(int,input().split())
    s = input()
    print(s[:k-1] + s[k-1].lower() + s[k:])

if __name__ == '__main__':
    problem126_a()