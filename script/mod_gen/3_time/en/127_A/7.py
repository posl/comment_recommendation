def main():
    #input
    A,B = map(int, input().split())
    #output
    if A>=13:
        print(B)
    elif A>=6:
        print(B//2)
    else:
        print(0)

if __name__ == '__main__':
    main()