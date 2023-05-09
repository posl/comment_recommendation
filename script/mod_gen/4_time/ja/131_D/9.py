def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    #a = [list(map(int, input().split())) for _ in range(n)]
    #s = input()
    #s = [input() for _ in range(n)]
    #n, m = map(int, input().split())
    #a = [list(map(int, input().split())) for _ in range(m)]
    #a = [int(input()) for _ in range(n)]
    #a = [list(map(int, input().split())) for _ in range(n)]
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort(key=lambda x:x[1])
    t = 0
    for i in range(n):
        t += a[i][0]
        if t > a[i][1]:
            print('No')
            exit()
    print('Yes')
    #print(t)
    #print(a)
    #print('Yes')
    #print('No')

if __name__ == '__main__':
    main()