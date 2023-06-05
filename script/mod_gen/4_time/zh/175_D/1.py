def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    visited = [False] * N
    cycles = []
    for i in range(N):
        if visited[i]:
            continue
        cycle = []
        j = i
        while not visited[j]:
            visited[j] = True
            cycle.append(C[P[j]-1])
            j = P[j]-1
        cycles.append(cycle)
    ans = -10**18
    for cycle in cycles:
        cycle.sort(reverse=True)
        s = sum(cycle)
        t = 0
        for i in range(len(cycle)):
            t += cycle[i]
            if i+1 > K:
                break
            now = t
            if s > 0:
                e = (K-(i+1))//len(cycle)
                now += s * e
            ans = max(ans, now)
    print(ans)

if __name__ == '__main__':
    main()