def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    count = 0
    for i in range(1, 31):
        for j in range(1, 31):
            for k in range(1, 31):
                if i + j + k == h1 and i + k + j == h2 and j + k + i == h3 and i + j + k == w1 and i + k + j == w2 and j + k + i == w3:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()