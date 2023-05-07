def main():
    N, M = map(int, input().split())
    correct = 0
    penalty = 0
    AC = [0] * (N+1)
    WA = [0] * (N+1)
    for i in range(M):
        p, S = input().split()
        p = int(p)
        if AC[p] == 0:
            if S == "AC":
                AC[p] = 1
                correct += 1
                penalty += WA[p]
            else:
                WA[p] += 1
    print(correct, penalty)

if __name__ == '__main__':
    main()