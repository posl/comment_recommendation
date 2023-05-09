def main():
    H, A = map(int, input().split())
    print(int((H + A - 1) / A))

if __name__ == '__main__':
    main()