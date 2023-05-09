def main():
    N = int(input())
    d = {}
    for i in range(N):
        x,y = map(int,input().split())
        d[(x,y)] = 1
    ans = 0
    for i in d:
        if d[i] == 1:
            ans += 1
            d[i] = 0
            stack = []
            stack.append(i)
            while stack:
                x,y = stack.pop()
                if (x-1,y-1) in d and d[(x-1,y-1)] == 1:
                    stack.append((x-1,y-1))
                    d[(x-1,y-1)] = 0
                if (x-1,y) in d and d[(x-1,y)] == 1:
                    stack.append((x-1,y))
                    d[(x-1,y)] = 0
                if (x,y-1) in d and d[(x,y-1)] == 1:
                    stack.append((x,y-1))
                    d[(x,y-1)] = 0
                if (x,y+1) in d and d[(x,y+1)] == 1:
                    stack.append((x,y+1))
                    d[(x,y+1)] = 0
                if (x+1,y) in d and d[(x+1,y)] == 1:
                    stack.append((x+1,y))
                    d[(x+1,y)] = 0
                if (x+1,y+1) in d and d[(x+1,y+1)] == 1:
                    stack.append((x+1,y+1))
                    d[(x+1,y+1)] = 0
    print(ans)
