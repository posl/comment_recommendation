def main():
    k,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(k+a[0])
    max_dis = 0
    for i in range(n):
        if max_dis < a[i+1]-a[i]:
            max_dis = a[i+1]-a[i]
    print(k-max_dis)

if __name__ == '__main__':
    main()