def main():
    S = input()
    S = list(S)
    S.sort()
    S = "".join(S)
    print(S)

if __name__ == '__main__':
    main()