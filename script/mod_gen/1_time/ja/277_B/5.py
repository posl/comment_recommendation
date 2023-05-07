def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if len(set(S)) != N:
        print("No")
        return
    if len(set([s[0] for s in S])) != 1:
        print("No")
        return
    if len(set([s[1] for s in S])) != 9:
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()