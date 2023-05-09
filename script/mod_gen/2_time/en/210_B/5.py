def main():
    N = int(input())
    S = input()
    print("Takahashi" if S.find("1") % 2 == 0 else "Aoki")

if __name__ == '__main__':
    main()