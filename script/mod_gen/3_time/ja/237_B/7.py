def main():
    h,w = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(h)]
    for i in range(w):
        print(*[a[j][i] for j in range(h)])

if __name__ == '__main__':
    main()