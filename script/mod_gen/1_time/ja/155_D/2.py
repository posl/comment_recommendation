def main():
    # input
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    # compute
    As.sort()
    if As[0] >= 0:
        ans = As[K-1] * As[K-2]
    elif As[-1] <= 0:
        ans = As[-K] * As[-K-1]
    else:
        ans = As[-1] * As[-2]
        for i in range(K):
            if As[i] * As[i+1] > ans:
                break
            ans = As[i] * As[i+1]
    # output
    print(ans)

if __name__ == '__main__':
    main()