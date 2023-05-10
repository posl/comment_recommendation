def main():
    P = list(map(int, input().split()))
    S = [chr(ord('a') + (p - 1)) for p in P]
    print(''.join(S))

if __name__ == '__main__':
    main()