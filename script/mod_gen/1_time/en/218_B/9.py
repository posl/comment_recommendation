def main():
    P = map(int, raw_input().split())
    S = [chr(96 + p) for p in P]
    print ''.join(S)

if __name__ == '__main__':
    main()