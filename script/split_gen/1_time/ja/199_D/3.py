def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    N,M = map(int,readline().split())
    if M == 0:
        print(3**N)
    else:
        AB = [list(map(int,readline().split())) for _ in range(M)]
        ab = set()
        for a,b in AB:
            ab.add((a,b))
            ab.add((b,a))
        #print(ab)
        ans = 0
        for i in range(3**N):
            color = []
            for j in range(N):
                color.append(i//(3**j)%3)
            #print(color)
            #print(i)
            flag = True
            for a,b in ab:
                if color[a-1] == color[b-1]:
                    flag = False
                    break
            if flag:
                ans += 1
        print(ans)
