def main():
    s = input()
    q = int(input())
    t_k = []
    for i in range(q):
        t_k.append(list(map(int, input().split())))
    #print(t_k)
    for i in range(q):
        t = t_k[i][0]
        k = t_k[i][1]
        for j in range(t):
            s = s.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
        print(s[k-1])

if __name__ == '__main__':
    main()