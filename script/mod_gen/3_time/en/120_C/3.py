def main():
    S = input()
    print(min(S.count('0'), S.count('1')) * 2)

if __name__ == '__main__':
    main()