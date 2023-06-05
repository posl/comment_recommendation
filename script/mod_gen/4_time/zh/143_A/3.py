def main():
    a,b = map(int, raw_input().split())
    print max(0, a-2*b)

if __name__ == '__main__':
    main()