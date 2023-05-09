def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = sum(a)
    b_sum = sum(b)
    a_list = []
    b_list = []
    for i in range(n):
        a_list.append([a_sum,sum(a[:i+1])])
        a_sum -= a[i]
    for i in range(m):
        b_list.append([b_sum,sum(b[:i+1])])
        b_sum -= b[i]
    ans = 0
    for i in range(n):
        if a_list[i][1] > k:
            break
        for j in range(m):
            if a_list[i][1]+b_list[j][1] > k:
                break
            if a_list[i][1]+b_list[j][1] <= k:
                ans = max(ans,i+j+2)
    print(ans)

if __name__ == '__main__':
    main()