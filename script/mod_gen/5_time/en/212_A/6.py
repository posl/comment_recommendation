def main():
    data = input()
    data = data.split()
    if (int(data[0]) > 0 and int(data[1]) == 0):
        print("Gold")
    elif (int(data[0]) == 0 and int(data[1]) > 0):
        print("Silver")
    else:
        print("Alloy")

if __name__ == '__main__':
    main()