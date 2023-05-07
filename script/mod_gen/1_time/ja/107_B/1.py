def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    for i in range(H):
        if "#" in A[i]:
            break
    else:
        print()
        exit()
    for i in range(i, H):
        for j in range(W):
            if A[i][j] == "#":
                break
        else:
            continue
        print("".join(A[i][j:]))

if __name__ == '__main__':
    main()