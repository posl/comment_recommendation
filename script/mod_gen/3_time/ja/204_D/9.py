def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    ovens = [0, 0]
    for t in T:
        if ovens[0] < ovens[1]:
            ovens[0] += t
        else:
            ovens[1] += t
    print(max(ovens))

if __name__ == '__main__':
    main()