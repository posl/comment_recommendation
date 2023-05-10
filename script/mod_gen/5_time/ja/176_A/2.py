def main():
    n,x,t = map(int, input().split())
    print(((n + x - 1) // x) * t)
    return

if __name__ == '__main__':
    main()