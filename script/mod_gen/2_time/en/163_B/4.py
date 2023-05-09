def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) > N:
        print(-1)
    else:
        print(N - sum(A))
main()
The second solution is the same as the first, but is written in a more compact way.

if __name__ == '__main__':
    main()