def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = sorted(A)
    print(A[1])

if __name__ == '__main__':
    main()