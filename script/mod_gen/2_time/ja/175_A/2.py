def main():
    S = input()
    if S == "RRR":
        print(3)
    elif S[0:2] == "RR" or S[1:3] == "RR":
        print(2)
    elif S[0] == "R" or S[1] == "R" or S[2] == "R":
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()