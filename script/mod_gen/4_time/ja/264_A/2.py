def main():
    L,R = map(int,input().split())
    S = input()
    print(S[L-1:R])

if __name__ == '__main__':
    main()