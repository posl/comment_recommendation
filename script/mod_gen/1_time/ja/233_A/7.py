def main():
    x, y = map(int, input().split())
    print(max(0, (y+9)//10-x//10))

if __name__ == '__main__':
    main()