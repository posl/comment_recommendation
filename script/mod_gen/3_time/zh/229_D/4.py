def main():
    S = input()
    K = int(input())
    S = S.replace('.', ' ')
    S = S.split(' ')
    S = [len(s) for s in S]
    S.sort(reverse=True)
    print(sum(S[:K]))

if __name__ == '__main__':
    main()