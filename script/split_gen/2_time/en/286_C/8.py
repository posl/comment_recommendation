def main():
    n, a, b = map(int, input().split())
    s = input()
    s = list(s)
    s.reverse()
    count = 0
    for i in range(n):
        if i == 0:
            continue
        if s[i] == s[i - 1]:
            count += a
        else:
            count += b
    print(count)
