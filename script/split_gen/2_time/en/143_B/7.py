def takoyaki_festival():
    N = int(input())
    d = list(map(int,input().split()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            ans += d[i]*d[j]
    print(ans)
    return
takoyaki_festival()
I solved this problem using the Python programming language.
I would like to receive your feedback on this problem.
I will be pleased if you could leave a comment.
Thank you for your cooperation.
