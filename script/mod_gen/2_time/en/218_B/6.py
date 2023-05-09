def main():
    P = [int(x) for x in input().split()]
    S = [chr(x+ord('a')-1) for x in P]
    print("".join(S))

if __name__ == '__main__':
    main()