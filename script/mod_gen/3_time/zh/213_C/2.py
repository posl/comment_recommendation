def main():
    h,w,n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    a1 = sorted(list(set(a)))
    b1 = sorted(list(set(b)))
    a2 = {}
    b2 = {}
    for i in range(len(a1)):
        a2[a1[i]] = i+1
    for i in range(len(b1)):
        b2[b1[i]] = i+1
    for i in range(n):
        print(a2[a[i]],b2[b[i]])

if __name__ == '__main__':
    main()