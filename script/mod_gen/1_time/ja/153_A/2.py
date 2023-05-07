def main():
    H, A = map(int, input().split())
    print(H//A if H%A == 0 else H//A + 1)

if __name__ == '__main__':
    main()