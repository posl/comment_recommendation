def main():
    S = input()
    Q = int(input())
    t = []
    k = []
    for i in range(Q):
        t_i, k_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)
    #print(S)
    #print(Q)
    #print(t)
    #print(k)
    for i in range(Q):
        S_i = S
        for j in range(t[i]):
            S_i = S_i.replace('a', 'bc')
            S_i = S_i.replace('b', 'ca')
            S_i = S_i.replace('c', 'ab')
        print(S_i[k[i]-1])
