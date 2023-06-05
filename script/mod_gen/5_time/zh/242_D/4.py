def main():
    s = input()
    q = int(input())
    t = []
    k = []
    for i in range(q):
        t_i,k_i = map(int,input().split())
        t.append(t_i)
        k.append(k_i)
    for i in range(q):
        s_i = s
        for j in range(t[i]):
            s_i = s_i.replace('a','bc')
            s_i = s_i.replace('b','ca')
            s_i = s_i.replace('c','ab')
        print(s_i[k[i]-1])

if __name__ == '__main__':
    main()