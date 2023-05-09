def main():
    n, q = map(int, input().split())
    s = input()
    l = []
    for i in range(n-1):
        if s[i:i+2] == "AC":
            l.append(1)
        else:
            l.append(0)
    for i in range(q):
        li, ri = map(int, input().split())
        print(sum(l[li-1:ri-1]))

if __name__ == '__main__':
    main()