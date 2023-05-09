def main():
    P = [int(x) for x in input().split()]
    S = [chr(x + 96) for x in P]
    print("".join(S))

if __name__ == '__main__':
    main()