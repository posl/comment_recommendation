def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    point = 0
    for i in range(n):
        if t[i] == "r":
            if i < k:
                point += p
            elif t[i-k] == "p":
                t = t[:i] + " " + t[i+1:]
            else:
                point += p
        elif t[i] == "s":
            if i < k:
                point += r
            elif t[i-k] == "r":
                t = t[:i] + " " + t[i+1:]
            else:
                point += r
        else:
            if i < k:
                point += s
            elif t[i-k] == "s":
                t = t[:i] + " " + t[i+1:]
            else:
                point += s
    print(point)

if __name__ == '__main__':
    main()