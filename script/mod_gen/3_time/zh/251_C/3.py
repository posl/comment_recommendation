def main():
    n = int(input())
    l = []
    for i in range(n):
        s,t = input().split()
        l.append((s,int(t)))
    l = sorted(l, key=lambda x: x[1], reverse=True)
    d = {}
    for i in range(n):
        if l[i][0] not in d:
            d[l[i][0]] = i+1
    print(d[l[0][0]])

if __name__ == '__main__':
    main()