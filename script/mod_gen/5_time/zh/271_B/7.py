def main():
    #n, q = map(int, input().split())
    #a = [list(map(int, input().split())) for _ in range(n)]
    #s = [list(map(int, input().split())) for _ in range(q)]
    n, q = 3, 4
    a = [[4, 128, 741, 239, 901],
         [2, 1, 1],
         [3, 314, 159, 26535]]
    s = [[1, 1],
         [2, 2],
         [3, 3],
         [1, 4]]
    for i in range(q):
        print(a[s[i][0]-1][s[i][1]-1])
main()
