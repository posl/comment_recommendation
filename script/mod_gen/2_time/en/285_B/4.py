def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        print(max([len(set(S[:j]) & set(S[j+i:])) for j in range(1,N-i)]+[0]))

if __name__ == '__main__':
    main()