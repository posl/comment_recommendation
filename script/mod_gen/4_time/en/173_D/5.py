def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum(A[1::2]))

if __name__ == '__main__':
    main()