def main():
    H, M = map(int, input().split())
    if H == 0 and M == 0:
        print("0 0")
    else:
        if M < 10:
            M = "0" + str(M)
        if H < 10:
            H = "0" + str(H)
        if M == "00":
            M = "0" + str(M)
        if H == "00":
            H = "0" + str(H)
        if M[0] == H[1] and M[1] == H[0]:
            print(H, M)
        else:
            if M[0] == H[1]:
                if int(M[1]) < 9:
                    print(H, int(M[1]) + 1)
                else:
                    print(int(H) + 1, "0" + str(0))
            elif M[1] == H[0]:
                if int(M[0]) < 5:
                    print(H, int(M[0]) + 1)
                else:
                    print(int(H) + 1, "0" + str(0))
            else:
                if int(M[0]) < 5:
                    print(H, int(M[0]) + 1)
                else:
                    print(int(H) + 1, "0" + str(0))
