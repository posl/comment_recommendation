def main():
    num = int(input())
    values = list(map(int, input().split()))
    values.sort()
    result = values[0]
    for i in range(1, num):
        result = (result + values[i]) / 2
    print(result)

if __name__ == '__main__':
    main()