def main():
    a,b = input().split()
    a = list(a)
    b = list(b)
    print(max(sum(map(int, a)), sum(map(int, b))))

if __name__ == '__main__':
    main()