def problem227_c():
    n = int(input())
    ans = 0
    for a in range(1, int(n ** (1/3)) + 1):
        for b in range(a, int(n ** (1/2)) + 1):
            if a * b > n:
                break
            ans += 1
    print(ans)

if __name__ == '__main__':
    problem227_c()