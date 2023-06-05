def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a = [0] + a
    b = [0] + b
    #print(a)
    #print(b)
    #print(n,m,k)
    #print(a[1])
    #print(b[2])
    #print(a[1] + b[2])
    ans = 0
    a_sum = 0
    b_sum = 0
    a_i = 0
    b_i = 0
    for i in range(1,n+1):
        a_sum += a[i]
        if a_sum > k:
            a_i = i - 1
            break
        else:
            a_i = i
    for j in range(1,m+1):
        b_sum += b[j]
        if b_sum > k:
            b_i = j - 1
            break
        else:
            b_i = j
    #print(a_i)
    #print(b_i)
    ans = max(a_i,b_i)
    #print(ans)
    a_sum = 0
    b_sum = 0
    for i in range(1,a_i+1):
        for j in range(1,b_i+1):
            if a_sum + b_sum + a[i] + b[j] > k:
                break
            else:
                ans = max(ans,i+j)
                b_sum += b[j]
        a_sum += a[i]
        b_sum = 0
    print(ans)

if __name__ == '__main__':
    main()