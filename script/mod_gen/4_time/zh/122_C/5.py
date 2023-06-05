def problem122_c():
    N, Q = map(int, input().split())
    S = input()
    #print(N, Q, S)
    #print(S[3:7].count("AC"))
    #print(S[2:3].count("AC"))
    #print(S[1:8].count("AC"))
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        #print(l_i, r_i)
        print(S[l_i-1:r_i].count("AC"))
problem122_c()
