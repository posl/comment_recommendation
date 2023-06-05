def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    flag = [0] * n
    for i in a:
        flag[i-1] += 1
    for i in l:
        if i == 1:
            if flag[0] == 0:
                flag[0] = 1
        else:
            if flag[i-1] == 0:
                flag[i-1] = 1
            else:
                flag[i-1] = 0
                flag[i] = 1
    for i in range(n):
        if flag[i] == 1:
            print(i+1,end=' ')
    print()

if __name__ == '__main__':
    main()