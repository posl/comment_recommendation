def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for i1 in range(1, 31):
        for i2 in range(1, 31):
            for i3 in range(1, 31):
                for i4 in range(1, 31):
                    for i5 in range(1, 31):
                        for i6 in range(1, 31):
                            for i7 in range(1, 31):
                                for i8 in range(1, 31):
                                    for i9 in range(1, 31):
                                        if i1 + i2 + i3 == h1 and i4 + i5 + i6 == h2 and i7 + i8 + i9 == h3 and i1 + i4 + i7 == w1 and i2 + i5 + i8 == w2 and i3 + i6 + i9 == w3:
                                            ans += 1
    print(ans)

if __name__ == '__main__':
    main()