def main():
    apples, pieces = map(int, input().split())
    print((apples*3+pieces)//2)

if __name__ == '__main__':
    main()