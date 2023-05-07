def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**18
    for i in range(N):
        total = 0
        cycle = [i]
        while P[cycle[-1]]-1 not in cycle:
            cycle.append(P[cycle[-1]]-1)
        for j in range(len(cycle)):
            total += C[cycle[j]]
            if total <= 0:
                continue
            temp = total*((K-j-1)//len(cycle))
            for k in range(K-j-1-(K-j-1)//len(cycle)*len(cycle)):
                temp += C[cycle[k]]
                ans = max(ans, temp)
    print(ans)

if __name__ == '__main__':
    main()