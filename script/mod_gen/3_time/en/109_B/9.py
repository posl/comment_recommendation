def shiritori():
    N = int(input())
    W = [input() for _ in range(N)]
    ans = "Yes"
    for i in range(N-1):
        if W[i] != W[i+1] and W[i][-1] != W[i+1][0]:
            ans = "No"
            break
    print(ans)
shiritori()
