def main():
    S = []
    for i in range(3):
        S.append(input())
    S.sort()
    if S[0] == S[1]:
        print(S[2])
    else:
        print(S[0])

if __name__ == '__main__':
    main()