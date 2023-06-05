def main():
    h,w = map(int,input().split())
    c = [input() for i in range(h)]
    for i in range(w):
        x = 0
        for j in range(h):
            if c[j][i] == '#':
                x += 1
        print(x,end=' ')
    print()

if __name__ == '__main__':
    main()