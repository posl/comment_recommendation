def main():
    P = list(map(int, input().split()))
    S = [chr(ord('a') + x - 1) for x in P]
    print(''.join(S))

if __name__ == '__main__':
    main()