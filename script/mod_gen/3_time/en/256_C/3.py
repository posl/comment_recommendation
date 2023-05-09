def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    count = 0
    for i1 in range(1, 30):
        for i2 in range(1, 30):
            for i3 in range(1, 30):
                if h1 == i1 + i2 + i3:
                    for j1 in range(1, 30):
                        for j2 in range(1, 30):
                            for j3 in range(1, 30):
                                if h2 == j1 + j2 + j3 and h3 == i1 + j1 + j2 + j3 and w1 == i1 + j1 and w2 == i2 + j2 and w3 == i3 + j3:
                                    count += 1
    print(count)

if __name__ == '__main__':
    main()