def main():
    h,w = map(int,input().split())
    s = [input() for i in range(h)]
    t = [input() for i in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()