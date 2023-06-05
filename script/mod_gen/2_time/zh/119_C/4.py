def get_input():
    num = int(input())
    result = 0
    for i in range(num):
        line = input().split()
        if line[1] == "BTC":
            result += float(line[0]) * 380000.0
        else:
            result += int(line[0])
    print(result)

if __name__ == '__main__':
    get_input()