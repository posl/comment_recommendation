def main():
    N = int(input())
    dic = {}
    for i in range(N):
        S,T = input().split()
        T = int(T)
        if S in dic:
            dic[S] = max(dic[S],T)
        else:
            dic[S] = T
    dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    print(dic[0][1])

if __name__ == '__main__':
    main()