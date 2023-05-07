def main():
    N = int(input())
    S = [input() for _ in range(N)]
    C = Counter(S)
    print(C.most_common(1)[0][0])

if __name__ == '__main__':
    main()