def main():
    sheep, wolf = map(int, input().split())
    if wolf >= sheep:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()