def solve():
    N,K = map(int,input().split())
    S = input()
    #print(N,K,S)
    happy_num = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy_num += 1
    #print(happy_num)
    happy_num += 2*K
    #print(happy_num)
    happy_num = min(happy_num,N-1)
    print(happy_num)
    return

if __name__ == '__main__':
    solve()