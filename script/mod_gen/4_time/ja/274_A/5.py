def main():
    A, B = map(int, input().split())
    print(str(round(B/A, 4))[:5])

if __name__ == '__main__':
    main()