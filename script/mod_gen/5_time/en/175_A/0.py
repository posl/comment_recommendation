def main():
    S = input()
    if S[0] == S[1] == S[2]:
        print(0)
    elif S[0] == S[1] or S[1] == S[2]:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()