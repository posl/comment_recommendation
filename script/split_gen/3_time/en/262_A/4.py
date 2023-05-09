def main():
    #input
    y = int(input())
    #calculate
    while True:
        if y % 4 == 2:
            break
        else:
            y += 1
    #output
    print(y)
main()
