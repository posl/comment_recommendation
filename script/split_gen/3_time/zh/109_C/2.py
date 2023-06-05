def main():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.append(x)
    x_list.sort()
    diff_list = []
    for i in range(n):
        diff_list.append(x_list[i+1] - x_list[i])
    if len(diff_list) == 1:
        print(diff_list[0])
    else:
        import math
        def gcd(a,b):
            if b == 0:
                return a
            else:
                return gcd(b,a%b)
        ans = diff_list[0]
        for i in range(1,n):
            ans = gcd(ans,diff_list[i])
        print(ans)
