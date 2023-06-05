def main():
    S = input()
    y = int(S[0:4])
    m = int(S[5:7])
    d = int(S[8:10])
    if y < 2019:
        print("Heisei")
    elif y == 2019 and m <= 4:
        print("Heisei")
    else:
        print("TBD")

if __name__ == '__main__':
    main()