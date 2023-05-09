def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 10**100
    S = [0] * len(B)
    S[0] = B[0]
    for i in range(1, len(B)):
        S[i] = S[i-1] + B[i]
        if S[i] > X:
            print(i+1)
            break

if __name__ == '__main__':
    main()