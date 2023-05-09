def main():
    # input
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    BCs = [list(map(int, input().split())) for _ in range(M)]
    # compute
    As.sort()
    BCs.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for B, C in BCs:
        for _ in range(B):
            if i >= N:
                break
            if As[i] >= C:
                break
            As[i] = C
            i += 1
    # output
    print(sum(As))

if __name__ == '__main__':
    main()