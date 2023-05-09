def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    B = list(zip(*A))
    C = ["".join(i) for i in B]
    i = 0
    j = 0
    while True:
        if i == H:
            break
        if "#" not in A[i]:
            del A[i]
            H -= 1
            continue
        i += 1
    while True:
        if j == W:
            break
        if "#" not in C[j]:
            for k in range(H):
                A[k] = A[k][:j] + A[k][j+1:]
            W -= 1
            continue
        j += 1
    for i in range(H):
        print(A[i])

if __name__ == '__main__':
    main()