def main():
    n,m,q = map(int,input().split())
    train = [0]*n
    for i in range(m):
        l,r = map(int,input().split())
        for j in range(l-1,r):
            train[j] += 1
    for i in range(q):
        p,q = map(int,input().split())
        count = 0
        for j in range(p-1,q):
            count += train[j]
        print(count)
main()
