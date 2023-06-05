def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N)
    #print(p)
    p_sort = sorted(p)
    #print(p_sort)
    cnt = 0
    for i in range(N):
        if p[i] != p_sort[i]:
            cnt += 1
    if cnt == 2 or cnt == 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()