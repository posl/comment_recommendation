def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = []
    for i in range(n):
        if i == 0:
            a.append(s[i])
        else:
            a.append(s[i] - sum(a))
    print(*a)
