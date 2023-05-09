def main():
    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    ans = 0
    for a in range(1, 31):
        for b in range(1, 31):
            for c in range(1, 31):
                for d in range(1, 31):
                    for e in range(1, 31):
                        for f in range(1, 31):
                            for g in range(1, 31):
                                for i in range(1, 31):
                                    for j in range(1, 31):
                                        if h[0] == a + b + c and h[1] == d + e + f and h[2] == g + i + j and w[0] == a + d + g and w[1] == b + e + i and w[2] == c + f + j:
                                            ans += 1
    print(ans)

if __name__ == '__main__':
    main()