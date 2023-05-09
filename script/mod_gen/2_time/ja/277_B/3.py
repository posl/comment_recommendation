def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if len(set(S)) == len(S):
        if all(s[0] in ['H', 'D', 'C', 'S'] for s in S):
            if all(s[1] in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'] for s in S):
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    main()