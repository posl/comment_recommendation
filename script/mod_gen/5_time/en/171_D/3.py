def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    total = sum(A)
    count = {}
    for a in A:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    for b, c in BC:
        if b in count:
            total += (c - b) * count[b]
            if c in count:
                count[c] += count[b]
            else:
                count[c] = count[b]
            count[b] = 0
        print(total)

if __name__ == '__main__':
    main()