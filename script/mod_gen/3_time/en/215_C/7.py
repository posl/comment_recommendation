def main():
    S, K = input().split()
    K = int(K)
    S = list(S)
    S.sort()
    S = ''.join(S)
    print(lexicographical_permutations(S, K))

if __name__ == '__main__':
    main()