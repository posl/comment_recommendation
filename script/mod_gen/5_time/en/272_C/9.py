def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = Counter(A)
    max_A = A.most_common()[0][0]
    if max_A % 2 == 1:
        max_A -= 1
    for a in A:
        if a == max_A:
            continue
        if max_A - a in A:
            print(max_A)
            exit()
    print(-1)

if __name__ == '__main__':
    main()