def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    AB = sorted(AB)
    AB = sorted(AB, key=lambda x:x[0])
    AB = sorted(AB, key=lambda x:x[1])
    
    ans = 1
    if N == 2:
        ans = 1
    else:
        ans = 2
        for i in range(1, len(AB)):
            if AB[i][0] == AB[i-1][0] and AB[i][1] == AB[i-1][1]:
                continue
            else:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()