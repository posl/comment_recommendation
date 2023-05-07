def  main():
    N, D = map(int, input().split())
    walls = []
    for  _  in  range(N):
        L, R = map(int, input().split())
        walls.append((L, R))
    walls.sort()
    ans = 0
    r = 0
    for  l, r  in  walls:
        if  r - l + 1  <=  D:
            ans += 1
            continue
        if  r  <  l + D - 1:
            continue
        if  r  <  l + D:
            ans += 1
            continue
        ans += 2
    print(ans)

if __name__ == '__main__':
    ()