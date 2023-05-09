def main():
    A, B = map(int, input().split())
    print("Easy" if A+B < 10 else "Hard")

if __name__ == '__main__':
    main()