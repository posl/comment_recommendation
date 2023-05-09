def main():
    L = int(input())
    if L % 2 == 0:
        k = L // 2 - 1
    else:
        k = L // 2
    print(sum([comb(k, i) for i in range(1, k+1)]))

if __name__ == '__main__':
    main()