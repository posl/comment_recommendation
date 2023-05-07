def main():
    N = int(input())
    S = [input() for i in range(N)]
    count = {}
    for s in S:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    print(max(count, key=lambda x: count[x]))

if __name__ == '__main__':
    main()