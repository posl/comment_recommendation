def main():
    x, k = map(int,input().split())
    result = x
    for i in range(k):
        result = round(result, -i - 1)
    print(result)

if __name__ == '__main__':
    main()