def main():
    #input
    N, M = map(int, input().split())
    SC = [list(map(int, input().split())) for _ in range(M)]
    #compute
    if N == 1:
        if M == 0:
            ans = 0
        else:
            ans = SC[0][1]
    else:
        if M == 0:
            ans = 10**(N-1)
        else:
            ans = -1
            for i in range(10**(N-1), 10**N):
                flag = True
                for j in range(M):
                    if int(str(i)[SC[j][0]-1]) != SC[j][1]:
                        flag = False
                        break
                if flag:
                    ans = i
                    break
    #output
    print(ans)

if __name__ == '__main__':
    main()