def main():
    A,B = map(int,input().split())
    print("Hard" if (A+B) >= 10**19 else "Easy")

if __name__ == '__main__':
    main()