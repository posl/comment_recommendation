def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[:K]) // K)

if __name__ == '__main__':
    main()