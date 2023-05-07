def main():
    A1,A2,A3 = map(int,input().split())
    print("win" if A1+A2+A3 <= 21 else "bust")

if __name__ == '__main__':
    main()