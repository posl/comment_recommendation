def main():
    s = input()
    q = int(input())
    t = []
    k = []
    for i in range(q):
        t_i, k_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)
    #print(s)
    #print(q)
    #print(t)
    #print(k)
    #print(s[0])
    for i in range(q):
        s_i = s
        t_i = t[i]
        k_i = k[i]
        for j in range(t_i):
            s_i = s_i.replace("A","BC")
            s_i = s_i.replace("B","CA")
            s_i = s_i.replace("C","AB")
        print(s_i[k_i-1])

if __name__ == '__main__':
    main()