def main():
    S = input()
    print("Yes" if all([S[i].islower() if i%2 else S[i].isupper() for i in range(len(S))]) else "No")

if __name__ == '__main__':
    main()