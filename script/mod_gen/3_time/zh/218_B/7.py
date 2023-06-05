def main():
    P = input().split()
    P = list(map(int, P))
    P = [chr(96 + i) for i in P]
    print(''.join(P))

if __name__ == '__main__':
    main()