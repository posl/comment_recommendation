def main():
    S = input()
    S = sorted(S)
    if S[0] == '1' and S[1] == '2' and S[2] == '3' and S[3] == '4' and S[4] == '5' and S[5] == '6' and S[6] == '7' and S[7] == '8' and S[8] == '9':
        print(0)
    elif S[0] == '2' and S[1] == '3' and S[2] == '4' and S[3] == '5' and S[4] == '6' and S[5] == '7' and S[6] == '8' and S[7] == '9':
        print(1)
    elif S[0] == '3' and S[1] == '4' and S[2] == '5' and S[3] == '6' and S[4] == '7' and S[5] == '8' and S[6] == '9':
        print(2)
    elif S[0] == '4' and S[1] == '5' and S[2] == '6' and S[3] == '7' and S[4] == '8' and S[5] == '9':
        print(3)
    elif S[0] == '5' and S[1] == '6' and S[2] == '7' and S[3] == '8' and S[4] == '9':
        print(4)
    elif S[0] == '6' and S[1] == '7' and S[2] == '8' and S[3] == '9':
        print(5)
    elif S[0] == '7' and S[1] == '8' and S[2] == '9':
        print(6)
    elif S[0] == '8' and S[1] == '9':
        print(7)
    elif S[0] == '9':
        print(8)
    else:
        print(9)

if __name__ == '__main__':
    main()