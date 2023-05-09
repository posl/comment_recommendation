def main():
    S = input()
    print(min(S.count('01'), S.count('10')) * 2)

if __name__ == '__main__':
    main()