def main():
    P = list(map(int, input().split()))
    S = [chr(96 + p) for p in P]
    print("".join(S))

if __name__ == '__main__':
    main()