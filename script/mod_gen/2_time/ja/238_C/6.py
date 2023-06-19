def  main():
    N = int(input())
    ans = 0
    for  i  in  range(1, 10):
        ans += (N - i) // 10 + 1
    print(ans % 998244353)
