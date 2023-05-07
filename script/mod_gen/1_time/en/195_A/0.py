def main():
    M, H = map(int, input().split())
    if H % M == 0:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()