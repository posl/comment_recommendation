def main():
    n = int(input())
    s = input()
    w = [int(i) for i in input().split()]
    #print(n,s,w)
    
    #初期化
    t = [0 for i in range(n)]
    for i in range(n):
        t[i] = 1 if s[i] == "1" else 0
    #print(t)
    
    #初期化
    ans = 0
    #Xを動かしていく
    for x in range(1,1000000001):
        #初期化
        cnt = 0
        #Xを動かしていく
        for i in range(n):
            if w[i] >= x and t[i] == 1:
                cnt += 1
            elif w[i] < x and t[i] == 0:
                cnt += 1
        if ans < cnt:
            ans = cnt
    print(ans)

if __name__ == '__main__':
    main()