def judge(n,k,q,a):
    ans = [0]*n
    score = k
    for i in a:
        ans[i-1] += 1
    for j in ans:
        if score - q + j > 0:
            print("Yes")
        else:
            print("No")
