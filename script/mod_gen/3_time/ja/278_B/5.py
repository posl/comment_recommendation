def main():
    H,M = map(int,input().split())
    if M >= 30:
        H += 1
        M -= 30
    else:
        M += 30
    if H >= 24:
        H -= 24
    print("{:02d} {:02d}".format(H,M))
main()

if __name__ == '__main__':
    main()