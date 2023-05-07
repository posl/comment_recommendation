def main():
    L = int(input())
    max_vol = 0
    for i in range(1,L):
        for j in range(1,L):
            k = L - i - j
            if k < 1:
                continue
            vol = i*j*k
            if vol > max_vol:
                max_vol = vol
    print(max_vol)

if __name__ == '__main__':
    main()