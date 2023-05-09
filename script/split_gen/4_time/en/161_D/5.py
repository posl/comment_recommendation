def solve():
    K = int(input())
    ans = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        for j in range(10):
            if ans[i]%10 == 0:
                if j == 0:
                    ans.append(ans[i]*10 + j)
                else:
                    ans.append(ans[i]*10 + j)
                    ans.append(ans[i]*10 + j - 1)
            elif ans[i]%10 == 9:
                if j == 9:
                    ans.append(ans[i]*10 + j)
                else:
                    ans.append(ans[i]*10 + j)
                    ans.append(ans[i]*10 + j + 1)
            else:
                ans.append(ans[i]*10 + j)
                ans.append(ans[i]*10 + j - 1)
                ans.append(ans[i]*10 + j + 1)
            ans.sort()
            if len(ans) >= K:
                break
    print(ans[K-1])
solve()
