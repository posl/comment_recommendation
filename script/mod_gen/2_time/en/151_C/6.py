def main():
    N, M = map(int, input().split())
    correct = [False] * N
    wa = [0] * N
    for _ in range(M):
        p, s = input().split()
        p = int(p) - 1
        if s == "AC":
            correct[p] = True
        elif not correct[p]:
            wa[p] += 1
    print(sum(correct), sum(wa[i] for i in range(N) if correct[i]))
main()

if __name__ == '__main__':
    main()