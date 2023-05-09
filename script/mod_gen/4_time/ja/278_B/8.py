def main():
    H,M = map(int,input().split())
    if M >= 32:
        if H == 23:
            print("00",M-32)
        else:
            print(H+1,M-32)
    else:
        print(H,M+28)

if __name__ == '__main__':
    main()