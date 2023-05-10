def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[:i] + S[i+1:] == T:
            print(i+1)
            break

if __name__ == '__main__':
    main()