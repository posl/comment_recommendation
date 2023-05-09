def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #Aの中身をカウントする
    Acount = [0] * (N+1)
    for i in range(N):
        Acount[A[i]] += 1
    #print(Acount)
    #Acountの中身をカウントする
    Acountcount = [0] * (N+1)
    for i in range(N+1):
        Acountcount[Acount[i]] += 1
    #print(Acountcount)
    #Acountcountの中身をカウントする
    Acountcountcount = [0] * (N+1)
    for i in range(N+1):
        Acountcountcount[Acountcount[i]] += 1
    #print(Acountcountcount)
    #Acountcountcountの中身をカウントする
    Acountcountcountcount = [0] * (N+1)
    for i in range(N+1):
        Acountcountcountcount[Acountcountcount[i]] += 1
    #print(Acountcountcountcount)
    #Acountcountcountcountの中身をカウントする
    Acountcountcountcountcount = [0] * (N+1)
    for i in range(N+1):
        Acountcountcountcountcount[Acountcountcountcount[i]] += 1
    #print(Acountcountcountcountcount)
    #Acountcountcountcountcountの中身をカウントする
    Acountcountcountcountcountcount = [0] * (N+1)
    for i in range(N+1):
        Acountcountcountcountcountcount[Acountcountcountcountcount[i]] += 1
    #print(Acountcountcountcountcountcount)
    #Acountcountcountcountcountcountの中身をカウントする
    Acountcountcountcountcountcountcount = [0] * (N+1)
    for i in range(N+1):
        Acountcountcountcountcountcountcount[Acountcountcountcountcountcount[i]] += 1
    #print(Acountcountcountcountcountcountcount)
    #Acountcountcountcountcountcountcountの中身をカウントする

if __name__ == '__main__':
    main()