def main():
    input = sys.stdin.readline
    S = input().rstrip('\n')
    print(S[1:] + S[0])

if __name__ == '__main__':
    main()