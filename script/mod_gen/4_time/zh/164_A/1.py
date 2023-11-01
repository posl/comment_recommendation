def main():
    S, W = map(int, input().split())
    if S <= W:
        print("unsafe")

if __name__ == '__main__':
    main()