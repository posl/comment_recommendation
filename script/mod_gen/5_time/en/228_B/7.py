def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(X-1, 0)
    friends = [0] * N
    for i in range(N):
        friends[A[i]-1] += 1
    print(friends)
    print(max(friends))

if __name__ == '__main__':
    main()