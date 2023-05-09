def main():
    N,K = map(int, input().split())
    a = []
    b = []
    c = []
    for i in range(1,N+1):
        if i%K == 0:
            a.append(i)
        elif i%K == K/2:
            b.append(i)
        else:
            c.append(i)
    print(len(a)**3 + len(b)**3 + len(c)**3 - len(b)*len(c)*len(a)*3)
