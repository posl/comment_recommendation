def main():
    n, m = map(int, input().split())
    correct = 0
    penalty = 0
    ac = [False] * (n + 1)
    wa = [0] * (n + 1)
    for _ in range(m):
        p, s = input().split()
        p = int(p)
        if ac[p]:
            continue
        if s == "AC":
            correct += 1
            penalty += wa[p]
            ac[p] = True
        else:
            wa[p] += 1
    print(correct, penalty)

if __name__ == '__main__':
    main()