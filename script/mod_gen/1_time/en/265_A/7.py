def main():
    x, y, n = map(int, input().split())
    print(min(x*(n//3*3), x*(n//3*3+3)-y*(n-(n//3*3))))

if __name__ == '__main__':
    main()