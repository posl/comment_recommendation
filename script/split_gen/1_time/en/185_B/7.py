def main():
    n,m,t = map(int,input().split())
    a = []
    b = []
    for _ in range(m):
        a_,b_ = map(int,input().split())
        a.append(a_)
        b.append(b_)
    charge = n
    for i in range(m):
        if i == 0:
            charge -= a[i]
            if charge <= 0:
                print('No')
                return
            charge += (b[i] - a[i])
            if charge > n:
                charge = n
        else:
            charge -= (a[i] - b[i-1])
            if charge <= 0:
                print('No')
                return
            charge += (b[i] - a[i])
            if charge > n:
                charge = n
    charge -= (t - b[-1])
    if charge <= 0:
        print('No')
    else:
        print('Yes')
