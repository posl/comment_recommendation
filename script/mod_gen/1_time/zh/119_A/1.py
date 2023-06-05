def problem119_a():
    S = input()
    S = S.split("/")
    if int(S[0]) < 2019:
        print("Heisei")
    elif int(S[0]) == 2019:
        if int(S[1]) < 4:
            print("Heisei")
        elif int(S[1]) == 4:
            if int(S[2]) <= 30:
                print("Heisei")
            else:
                print("TBD")
        else:
            print("TBD")
    else:
        print("TBD")

if __name__ == '__main__':
    problem119_a()