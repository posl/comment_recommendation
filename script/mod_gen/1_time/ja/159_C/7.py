def main():
    L = int(input())
    res = 0
    for i in range(1, L):
        for j in range(1, L):
            if i * j > L:
                break
            k = L - i * j
            res = max(res, i * j * k)
    print(res)

if __name__ == '__main__':
    main()