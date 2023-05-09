def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    h = [h1, h2, h3]
    w = [w1, w2, w3]
    cnt = 0
    for i1 in range(1, 31):
        for i2 in range(1, 31):
            for i3 in range(1, 31):
                for i4 in range(1, 31):
                    for i5 in range(1, 31):
                        for i6 in range(1, 31):
                            for i7 in range(1, 31):
                                for i8 in range(1, 31):
                                    for i9 in range(1, 31):
                                        if h1 == i1 + i2 + i3 and h2 == i4 + i5 + i6 and h3 == i7 + i8 + i9 and w1 == i1 + i4 + i7 and w2 == i2 + i5 + i8 and w3 == i3 + i6 + i9:
                                            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()