def main():
    n = int(input())
    for i in range(n):
        print(*pascal_triangle(i+1))

if __name__ == '__main__':
    main()