def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [[a[j][i] for j in range(h)] for i in range(w)]
    for i in range(w):
        print(*b[i])

if __name__ == '__main__':
    main()