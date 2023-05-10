def main():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.append(x)
    x_list.sort()
    diff_list = []
    for i in range(n):
        diff_list.append(x_list[i+1]-x_list[i])
    import math
    ans = math.gcd(diff_list[0],diff_list[1])
    for i in range(2,n):
        ans = math.gcd(ans,diff_list[i])
    print(ans)
