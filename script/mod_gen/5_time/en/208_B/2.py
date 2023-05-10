def main():
    p = int(input())
    coin = [1,2,6,24,120,720,5040,40320,362880,3628800]
    count = 0
    for i in range(9,-1,-1):
        if coin[i] <= p:
            count += p // coin[i]
            p = p % coin[i]
    print(count)

if __name__ == '__main__':
    main()