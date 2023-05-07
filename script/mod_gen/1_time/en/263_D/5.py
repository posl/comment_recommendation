def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A = [max(min(R, a), L) for a in A]
    print(sum(A))

if __name__ == '__main__':
    main()