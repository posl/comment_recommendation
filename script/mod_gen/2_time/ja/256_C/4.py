def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for i1 in range(1, 31):
        for i2 in range(1, 31):
            for i3 in range(1, 31):
                if h1 == i1 + i2 + i3:
                    if h2 == i1 + i2 + i3 + i1 + i2 + i3:
                        if h3 == i2 + i3 + i1 + i2 + i3 + i1:
                            if w1 == i1 + i2 + i1:
                                if w2 == i2 + i3 + i2:
                                    if w3 == i3 + i1 + i3:
                                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()