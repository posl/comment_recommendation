def main():
    N = int(input())
    a = list(map(int, input().split()))
    #a = [3, 2, 3, 2, 2]
    #a = [2, 3, 2, 3, 3, 3, 2, 3, 3, 2]
    #N = len(a)
    a.reverse()
    a.append(0)
    a.reverse()
    #print(a)
    #print(N)
    ans = [0] * N
    ans[0] = 1
    #print(ans)
    for i in range(1, N):
        if a[i] > a[i-1]:
            ans[i] = ans[i-1] + 1
        elif a[i] == a[i-1]:
            ans[i] = ans[i-1]
        else:
            ans[i] = ans[i-1] - 1
    #print(ans)
    ans.reverse()
    print(*ans, sep='\n')
