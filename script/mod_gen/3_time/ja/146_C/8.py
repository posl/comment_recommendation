def main():
    a, b, x = map(int, input().split())
    print(int((x - b) / a)) if x >= a else print(0)

if __name__ == '__main__':
    main()