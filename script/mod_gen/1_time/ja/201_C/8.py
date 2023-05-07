def main():
    S = input()
    #print(S)
    count = 0
    for i in range(0,10):
        if S[i] == "o":
            count += 1
    #print(count)
    if count > 4:
        print(0)
        return
    elif count == 4:
        print(24)
        return
    elif count == 3:
        print(36)
        return
    elif count == 2:
        print(14)
        return
    elif count == 1:
        print(1)
        return
    else:
        print(0)
        return

if __name__ == '__main__':
    main()