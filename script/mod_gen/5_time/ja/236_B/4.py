def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[(2*N)-1])

if __name__ == '__main__':
    main()