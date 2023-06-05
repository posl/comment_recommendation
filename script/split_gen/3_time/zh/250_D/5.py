def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N ** 0.25) + 1):
        if N % i == 0:
            for j in range(i + 1, int(N ** 0.5) + 1):
                if N % (i * j ** 3) == 0:
                    ans += 1
    print(ans)
