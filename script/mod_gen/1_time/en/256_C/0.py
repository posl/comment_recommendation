def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for i in range(1, 31):
        for j in range(1, 31):
            if h1 == i + j and w1 == i + j:
                for k in range(1, 31):
                    if h2 == i + j + k and w2 == i + j + k:
                        if h3 == i + k and w3 == j + k:
                            ans += 1
    print(ans)

if __name__ == '__main__':
    main()