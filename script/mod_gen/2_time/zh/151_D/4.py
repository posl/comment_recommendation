def main():
    n,m = map(int,input().split())
    p = [0]*n
    s = [0]*n
    for i in range(m):
        pi,si = input().split()
        pi = int(pi)
        if si == 'AC':
            if p[pi-1] == 0:
                p[pi-1] = 1
        else:
            if p[pi-1] == 0:
                s[pi-1] += 1
    print(sum(p),sum([p[i]*s[i] for i in range(n)]))

if __name__ == '__main__':
    main()