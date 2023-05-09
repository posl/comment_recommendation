def main():
    N = int(input())
    T = [int(x) for x in input().split()]
    T.sort()
    if N == 1:
        print(T[0])
    elif N == 2:
        print(max(T))
    else:
        print(sum(T) - min(T))

if __name__ == '__main__':
    main()