def main():
    # input
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    # compute
    total = sum(As)
    As.sort(reverse=True)
    if As[M-1] >= total / (4*M):
        ans = 'Yes'
    else:
        ans = 'No'
    # output
    print(ans)

if __name__ == '__main__':
    main()