def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = []
    for _ in range(M):
        BC.append(list(map(int, input().split())))
    A.sort(reverse = True)
    BC.sort(key = lambda x: x[1], reverse = True)
    card = 0
    for b, c in BC:
        for _ in range(b):
            if card >= N:
                break
            if A[card] < c:
                A[card] = c
                card += 1
            else:
                break
    print(sum(A))

if __name__ == '__main__':
    main()