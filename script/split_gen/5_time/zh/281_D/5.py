def main():
    n,k,d = map(int,input().split())
    a_list = list(map(int,input().split()))
    ans = -1
    for i in range(n-k+1):
        b_list = a_list[i:i+k]
        if sum(b_list)%d != 0:
            ans = max(ans,sum(b_list))
    print(ans)
