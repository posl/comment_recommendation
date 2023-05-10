def main():
    S = input()
    K = int(input())
    S = S.replace(".", " ")
    S = S.split()
    S = "".join(S)
    S = S.split("X")
    S = [len(s) for s in S]
    S.sort(reverse=True)
    print(min(S[0] + K, len(S)))

if __name__ == '__main__':
    main()