def main():
    p = list(map(int,input().split()))
    print("".join(sorted([chr(i+96) for i in p])))
main()

if __name__ == '__main__':
    main()