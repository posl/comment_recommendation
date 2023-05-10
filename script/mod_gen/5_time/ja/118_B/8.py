def main():
    N,M = map(int,input().split())
    #print(N,M)
    result = 0
    like_list = []
    for i in range(N):
        like_list.append(list(map(int,input().split())))
    #print(like_list)
    for i in range(1,M+1):
        #print(i)
        for j in range(N):
            #print(like_list[j])
            if i in like_list[j][1:]:
                #print("OK")
                if j == N-1:
                    #print("OK")
                    result += 1
            else:
                break
    print(result)

if __name__ == '__main__':
    main()