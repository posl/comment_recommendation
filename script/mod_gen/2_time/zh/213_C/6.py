def main():
    H, W, N = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [a for a, _ in AB]
    B = [b for _, b in AB]
    A = sorted(set(A))
    B = sorted(set(B))
    A = {a: i + 1 for i, a in enumerate(A)}
    B = {b: i + 1 for i, b in enumerate(B)}
    for a, b in AB:
        print(A[a], B[b])

if __name__ == '__main__':
    main()