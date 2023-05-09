def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 100
    total = 0
    for i in range(len(B)):
        total += B[i]
        if total > X:
            print(i+1)
            break

if __name__ == '__main__':
    main()