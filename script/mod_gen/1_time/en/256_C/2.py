def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    count = 0
    for i in range(1, 31):
        for j in range(1, 31):
            for k in range(1, 31):
                if i + j + k == h1:
                    if i + j + k == h2:
                        if i + j + k == h3:
                            if i + i + i == w1:
                                if j + j + j == w2:
                                    if k + k + k == w3:
                                        count += 1
    print(count)

if __name__ == '__main__':
    main()