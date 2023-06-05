def main():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    sum = 0
    for i in range(N):
        sum += a[i]
        if sum > X:
            print("No")
            exit()
        sum += (b[i] - a[i])
    if sum > X:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()