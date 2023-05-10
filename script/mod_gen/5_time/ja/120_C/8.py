def main():
    S = input()
    #print(S)
    count = 0
    while True:
        if S.find("01") == -1 and S.find("10") == -1:
            break
        if S.find("01") != -1:
            S = S.replace("01","",1)
            count += 1
        if S.find("10") != -1:
            S = S.replace("10","",1)
            count += 1
    print(count)
main()

if __name__ == '__main__':
    main()