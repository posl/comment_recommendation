def main():
    N = int(input())
    p = list(map(int,input().split()))
    #print(N,p)
    cnt = 0
    for i in range(N):
        if p[i] == i:
            cnt += 1
    if cnt == N:
        print(cnt)
    elif cnt == N-2:
        print(cnt+2)
    else:
        print(cnt+1)

if __name__ == '__main__':
    main()