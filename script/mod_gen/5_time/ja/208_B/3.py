def main():
    n = int(input())
    #n!のリストを作成
    n_list = [1]
    for i in range(1,11):
        n_list.append(n_list[i-1]*i)
    #print(n_list)
    #n!のリストから引いていく
    ans = 0
    for i in range(10,0,-1):
        #print(n_list[i])
        while n >= n_list[i]:
            n -= n_list[i]
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()