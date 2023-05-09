def main():
    # input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # compute
    A.sort()
    A.append(M)
    B = []
    prev = -1
    count = 0
    for a in A:
        if a == prev:
            count += 1
        else:
            if prev != -1:
                B.append(count)
            count = 1
            prev = a
    B.sort(reverse=True)
    if len(B) == 1:
        ans = B[0]
    elif len(B) == 2:
        ans = B[0] + B[1]
    else:
        ans = B[0] + B[1] + B[2]
    ans = N - ans
    print(ans)

if __name__ == '__main__':
    main()