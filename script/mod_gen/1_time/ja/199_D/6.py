def main():
    import sys
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        a, b = map(int, input().split())
        AB.append([a, b])
    
    ans = 0
    for i in range(3 ** N):
        tmp = i
        color = []
        for j in range(N):
            color.append(tmp % 3)
            tmp //= 3
        
        flag = 0
        for j in range(M):
            if color[AB[j][0] - 1] == color[AB[j][1] - 1]:
                flag = 1
        
        if flag == 0:
            ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()