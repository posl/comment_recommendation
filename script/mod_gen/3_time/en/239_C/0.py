def main():
    x_1, y_1, x_2, y_2 = map(int, input().split())
    if ((x_1 - x_2)**2 + (y_1 - y_2)**2)**(1/2) == ((x_1)**2 + (y_1)**2)**(1/2) + ((x_2)**2 + (y_2)**2)**(1/2):
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()