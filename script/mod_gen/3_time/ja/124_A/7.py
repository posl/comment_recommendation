def main():
    a, b = map(int, input().split())
    print(max((a*2-1),(b*2-1),a+b))

if __name__ == '__main__':
    main()