def main():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.append(x)
    x_list.sort()
    ans = x_list[1]-x_list[0]
    for i in range(1,n+1):
        ans = gcd(ans,x_list[i]-x_list[i-1])
    print(ans)
