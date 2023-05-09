def main():
    #n, q = map(int, input().split())
    #l = [list(map(int, input().split())) for _ in range(n)]
    #s = [list(map(int, input().split())) for _ in range(q)]
    n, q = 2, 2
    l = [[3, 1, 4, 7], [2, 5, 9]]
    s = [[1, 3], [2, 1]]
    for i in range(q):
        print(l[s[i][0]-1][s[i][1]-1])

if __name__ == '__main__':
    main()