def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    #print(d)
    #print(N)
    if N%2 == 0:
        #偶数
        #print("even")
        #print(d[N//2-1])
        #print(d[N//2])
        ans = d[N//2] - d[N//2-1]
        print(ans)
    else:
        #奇数
        #print("odd")
        print(0)
