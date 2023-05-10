def solve():
    N = int(input())
    snukes = []
    for i in range(N):
        t, x, a = map(int, input().split())
        snukes.append((t, x, a))
    #print(snukes)
    snukes.sort()
    #print(snukes)
    #print(snukes[-1])
    max_size = 0
    for i in range(N):
        t, x, a = snukes[i]
        #print("t, x, a:", t, x, a)
        if t > x:
            continue
        elif t == x:
            max_size += a
        else:
            max_size += a
            for j in range(i+1, N):
                t, x, a = snukes[j]
                #print("t, x, a:", t, x, a)
                if t > x:
                    continue
                elif t == x:
                    max_size += a
                else:
                    break
            break
    print(max_size)

if __name__ == '__main__':
    solve()