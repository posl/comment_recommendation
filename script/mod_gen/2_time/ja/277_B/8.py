def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #print(N)
    #print(S)
    if len(set(S)) == N:
        if all(x[0] in ('H', 'D', 'C', 'S') for x in S):
            if all(x[1] in ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K') for x in S):
                print("Yes")
                return
    print("No")
    return

if __name__ == '__main__':
    main()