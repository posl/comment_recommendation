def main():
    n = int(input())
    seq = []
    for i in range(n):
        seq.append([int(x) for x in input().split()])
    seq.sort()
    prev = seq[0]
    count = 1
    for i in range(1, n):
        if seq[i] != prev:
            count += 1
            prev = seq[i]
    print(count)

if __name__ == '__main__':
    main()