def main():
    S = input()
    T = input()
    print(sum([1 for i in range(3) if S[i] == T[i]]))

if __name__ == '__main__':
    main()