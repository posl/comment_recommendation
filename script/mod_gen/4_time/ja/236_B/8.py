def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[(4*N-1)//2])

if __name__ == '__main__':
    main()