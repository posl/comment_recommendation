def main():
    #input
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = map(str, input().split())
        S.append(s)
        T.append(int(t))
    #process
    t_max = max(T)
    T.remove(t_max)
    t_max2 = max(T)
    i_max2 = T.index(t_max2)
    #output
    print(S[i_max2])
