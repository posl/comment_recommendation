def main():
    S, T, X = map(int, input().split())
    if X >= S and X+1 <= T:
        print('Yes')
    else:
        print('No')
main()
