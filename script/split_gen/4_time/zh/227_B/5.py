def main():
    n = int(input())
    s = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(1, 32):
            for k in range(1, 32):
                if s[i] == 4 * j * k + 3 * j + 3 * k:
                    cnt += 1
    print(n - cnt)
