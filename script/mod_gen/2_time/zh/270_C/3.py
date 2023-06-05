def main():
    input_list = input().split()
    x = int(input_list[0])
    y = int(input_list[1])
    z = int(input_list[2])
    if (x > 0 and x > y) or (x < 0 and x < y):
        print(abs(x - y) + abs(y - z))
    else:
        print(-1)

if __name__ == '__main__':
    main()