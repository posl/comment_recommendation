def main():
    H,A = map(int,input().split())
    if H%A == 0:
        print(H//A)
    else:
        print(H//A+1)

if __name__ == '__main__':
    main()