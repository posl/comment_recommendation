def main():
    x_1, x_2, x_3, x_4, x_5 = map(int, input().split())
    for i in range(1, 6):
        if eval("x_" + str(i)) == 0:
            print(i)
            break

if __name__ == '__main__':
    main()