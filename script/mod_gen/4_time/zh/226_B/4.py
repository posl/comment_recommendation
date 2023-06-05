def main():
    N = int(input())
    seq = []
    for i in range(N):
        seq.append(list(map(int, input().split()))[1:])
    seq.sort()
    count = 1
    for i in range(N-1):
        if seq[i] != seq[i+1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()