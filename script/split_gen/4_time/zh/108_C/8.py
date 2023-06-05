def main():
    n,k = map(int,input().split())
    ans = 0
    # 1~n
    for i in range(1,n+1):
        # 1~k
        for j in range(1,k+1):
            if i%j == 0:
                # 1~k
                for l in range(1,k+1):
                    if i%l == 0:
                        ans += 1
    print(ans)
