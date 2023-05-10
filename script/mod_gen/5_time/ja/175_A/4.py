def main():
    S = input()
    S = S.replace('R',' ')
    S = S.split()
    print(len(S[0]))

if __name__ == '__main__':
    main()