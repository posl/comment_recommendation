def main():
    S = input()
    T = input()
    if len(S) == len(T):
        if T in S + S:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()