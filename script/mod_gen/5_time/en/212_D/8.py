def main():
    # input
    n = int(input())
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))
    #s = input()
    #s = input().split()
    #a = [int(input()) for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]
    #a = [int(input()) for i in range(h)]
    #a = [list(map(int, input().split())) for i in range(h)]
    #a = [input() for i in range(h)]
    #a = [input().split() for i in range(h)]
    #a = [list(map(int, input().split())) for i in range(h)]
    #a = [list(map(int, input().split())) for i in range(h)]
    #a = [list(map(int, input().split())) for i in range(h)]
    # solve
    import heapq
    hq = []
    add = 0
    for i in range(n):
        p = input().split()
        if p[0] == '1':
            heapq.heappush(hq, int(p[1]) - add)
        elif p[0] == '2':
            add += int(p[1])
        else:
            print(heapq.heappop(hq) + add)
    # output

if __name__ == '__main__':
    main()