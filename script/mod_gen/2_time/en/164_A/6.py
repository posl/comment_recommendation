def main():
    s, w = map(int, input().split())
    if s > w:
        print("safe")
    else:
        print("unsafe")
main()

if __name__ == '__main__':
    main()