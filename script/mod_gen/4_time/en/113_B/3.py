def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    print(min(range(N), key=lambda i:abs(A-(T-H[i]*0.006)))+1)

if __name__ == '__main__':
    main()