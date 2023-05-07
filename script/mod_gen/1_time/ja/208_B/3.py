def main():
    P = int(input())
    coins = [1,2,6,24,120,720,5040,40320,362880,3628800]
    cnt = 0
    for i in range(10):
        cnt += P//coins[9-i]
        P = P%coins[9-i]
    print(cnt)

if __name__ == '__main__':
    main()