def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = [0] * 100001
    for v in V:
        C[v] += 1
    V.sort()
    V = V[N//2:]
    if V[0] == V[-1]:
        print(N//2)
    else:
        print(N - max(C[V[0]], C[V[-1]]))

if __name__ == '__main__':
    main()