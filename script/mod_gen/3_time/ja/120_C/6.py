def main():
    N = int(input())
    S = input()
    print(max(S.count('0'), S.count('1'))*2)

if __name__ == '__main__':
    main()