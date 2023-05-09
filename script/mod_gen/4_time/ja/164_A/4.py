def main():
    s, w = map(int, input().split())
    print("unsafe" if s <= w else "safe")

if __name__ == '__main__':
    main()