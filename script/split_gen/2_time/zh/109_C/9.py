def main():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.append(x)
    x_list.sort()
    x_list = [x_list[i+1]-x_list[i] for i in range(n)]
    x_list = x_list[::-1]
    ans = x_list[0]
    for i in range(1,n):
        ans = gcd(ans,x_list[i])
    print(ans)
