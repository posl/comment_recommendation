def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    t.sort()
    t = t[:n]
    for i in range(n):
        if t[i] < s[i]:
            t[i] = s[i]
    print(min(t))
