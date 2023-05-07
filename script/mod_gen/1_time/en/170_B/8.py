def main():
    inputs = input().split()
    x = int(inputs[0])
    y = int(inputs[1])
    if x*2 == y or x*4 == y or x*2 + x*4 == y:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()