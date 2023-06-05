def main():
    h1,w1 = map(int,input().split())
    a = []
    for i in range(h1):
        a.append(list(map(int,input().split())))
    h2,w2 = map(int,input().split())
    b = []
    for i in range(h2):
        b.append(list(map(int,input().split())))
    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            temp = []
            for k in range(h2):
                temp.append(a[i+k][j:j+w2])
            if temp == b:
                print("Yes")
                return
    print("No")
    return

if __name__ == '__main__':
    main()