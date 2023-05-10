def main():
    S, W = map(int, input().split())
    print("safe" if S > W else "unsafe")

if __name__ == '__main__':
    main()