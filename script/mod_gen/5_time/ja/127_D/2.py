def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    c = []
    for i in range(m):
        b_i,c_i = map(int,input().split())
        b.append(b_i)
        c.append(c_i)
    b_c = list(zip(b,c))
    b_c.sort(key=lambda x:x[1],reverse=True)
    sum = 0
    for i in range(len(b_c)):
        for j in range(b_c[i][0]):
            if a[j] < b_c[i][1]:
                a[j] = b_c[i][1]
            else:
                break
    for i in range(n):
        sum += a[i]
    print(sum)

if __name__ == '__main__':
    main()