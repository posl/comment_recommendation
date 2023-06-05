def main():
    s = input()
    q = int(input())
    t_k = []
    for i in range(q):
        t_k.append(list(map(int, input().split())))
    # print(t_k)
    for i in range(q):
        s = S(s, t_k[i][0])
        print(s[t_k[i][1]-1])

if __name__ == '__main__':
    main()