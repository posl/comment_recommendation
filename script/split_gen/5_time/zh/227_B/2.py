def main():
    n = int(input())
    s = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if s[i] == 4:
            cnt += 1
            continue
        for a in range(1, 1000):
            for b in range(1, 1000):
                if 4 * a * b + 3 * a + 3 * b == s[i]:
                    cnt += 1
    print(n - cnt)
