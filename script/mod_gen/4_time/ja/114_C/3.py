def main():
    N = int(input())
    ans = 0
    for i in range(3, 10):
        for j in range(3, 10):
            for k in range(3, 10):
                for l in range(3, 10):
                    for m in range(3, 10):
                        for n in range(3, 10):
                            for o in range(3, 10):
                                for p in range(3, 10):
                                    num = 10000000 * i + 1000000 * j + 100000 * k + 10000 * l + 1000 * m + 100 * n + 10 * o + p
                                    if num <= N and (i == 7 or j == 7 or k == 7 or l == 7 or m == 7 or n == 7 or o == 7 or p == 7) and (i == 5 or j == 5 or k == 5 or l == 5 or m == 5 or n == 5 or o == 5 or p == 5) and (i == 3 or j == 3 or k == 3 or l == 3 or m == 3 or n == 3 or o == 3 or p == 3):
                                        ans += 1
    print(ans)
main()
