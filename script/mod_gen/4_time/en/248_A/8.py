def main():
    S = input().split()
    S = S[0]
    S = list(S)
    S = [int(s) for s in S]
    for i in range(1,10):
        if i not in S:
            print(i)
            break

if __name__ == '__main__':
    main()