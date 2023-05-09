def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    #累積和を求める
    sum_a = [0]*(n+1)
    for i in range(n):
        sum_a[i+1] = sum_a[i] + a[i]
    #P,Q,Rの最大値を求める
    max_p = max_q = max_r = 0
    for i in range(n):
        max_p = max(max_p, sum_a[i+1]-sum_a[0])
        max_q = max(max_q, sum_a[i+1]-sum_a[max(0,i-p+1)])
        max_r = max(max_r, sum_a[i+1]-sum_a[max(0,i-q+1)])
    #P,Q,Rの最大値になる組を求める
    max_pq = max_pr = max_qr = 0
    for i in range(n):
        max_pq = max(max_pq, sum_a[i+1]-sum_a[max(0,i-p+1)]+max_q)
        max_pr = max(max_pr, sum_a[i+1]-sum_a[max(0,i-q+1)]+max_r)
        max_qr = max(max_qr, sum_a[i+1]-sum_a[max(0,i-r+1)]+max_p)
    #P,Q,Rの最大値になる組が条件を満たすか判定する
    if max_p+max_q+max_r < max_pq+max_pr+max_qr:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()