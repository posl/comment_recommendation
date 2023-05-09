def main():
    H,M = map(int,input().split())
    if M == 0:
        print(H,M)
        return
    if M <= 9:
        print(H,0,M)
        return
    if M <= 19:
        print(H,1,M-10)
        return
    if M <= 29:
        print(H,2,M-20)
        return
    if M <= 39:
        print(H,3,M-30)
        return
    if M <= 49:
        print(H,4,M-40)
        return
    if M <= 59:
        print(H,5,M-50)
        return

if __name__ == '__main__':
    main()