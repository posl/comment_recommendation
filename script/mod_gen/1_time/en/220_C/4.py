def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 100000
    #print(B)
    sum = 0
    for i in range(1000000):
        sum += B[i]
        if sum > X:
            print(i+1)
            break

if __name__ == '__main__':
    main()