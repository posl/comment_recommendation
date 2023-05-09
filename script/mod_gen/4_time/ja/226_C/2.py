def main():
    n = int(input())
    t = []
    k = []
    a = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        t.append(tmp[0])
        k.append(tmp[1])
        a.append(tmp[2:])
    #print(t)
    #print(k)
    #print(a)
    #print()
    #print()
    #print()
    #t = [3, 5, 7]
    #k = [0, 1, 1]
    #a = [[], [1], [1]]
    #t = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    #k = [0, 0, 0, 0, 4]
    #a = [[], [], [], [], [1, 2, 3, 4]]
    #print(t)
    #print(k)
    #print(a)
    #print()
    #print()
    #print()
    #t = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    #k = [0, 0, 0, 0, 4]
    #a = [[], [], [], [], [1, 2, 3, 4]]
    #print(t)
    #print(k)
    #print(a)
    #print()
    #print()
    #print()
    #n = 200000
    #t = [1000000000 for _ in range(n)]
    #k = [0 for _ in range(n)]
    #a = [[] for _ in range(n)]
    #a[-1] = [i for i in range(1, n)]
    #print(t)
    #print(k)
    #print(a)
    #print()
    #print()
    #print()
    #n = 200000
    #t = [1000000000 for _ in range(n)]
    #k = [0 for _ in range(n)]
    #a = [[] for _ in range(n)]
    #a[-1] = [i for i in range(1, n)]
    #print(t)
    #print(k)
    #print(a)
    #print()

if __name__ == '__main__':
    main()