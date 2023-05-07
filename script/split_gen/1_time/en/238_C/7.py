def  main():
    N = int(input())
    ans = 0
    for  i in range(1, 19):
         if  N < 10 ** i:
            ans += solve(N, i)
             break 
        ans += solve(10 ** i - 1, i)
    print(ans % 998244353)
