def main():
    n, m = map(int, input().split())
    max = n * n
    s = [max] * max
    s[0] = 0
    for i in range(max):
        for j in range(max):
            if s[j] > s[i] + 1 and ((i // n - j // n) ** 2 + (i % n - j % n) ** 2) ** 0.5 <= m:
                s[j] = s[i] + 1
    for i in range(max):
        if s[i] == max:
            s[i] = -1
    print(*s)
