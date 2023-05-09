def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    friends = [0] * (N + 1)
    friends[X] = 1
    for i in range(1, N + 1):
        if friends[i] == 1:
            friends[A[i]] = 1
    print(sum(friends))
main()

if __name__ == '__main__':
    main()