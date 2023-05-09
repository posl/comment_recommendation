def main():
    P = [int(i) for i in input().split()]
    S = [chr(97+i-1) for i in P]
    print("".join(S))

if __name__ == '__main__':
    main()