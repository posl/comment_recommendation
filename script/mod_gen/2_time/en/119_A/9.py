def main():
    #Get input
    inp = input()
    #Split input into array
    inp = inp.split("/")
    #Check if month is less than 4
    if int(inp[1]) < 4:
        print("Heisei")
    #Check if month is 4 and day is less than 30
    elif int(inp[1]) == 4 and int(inp[2]) < 30:
        print("Heisei")
    #Otherwise print TBD
    else:
        print("TBD")

if __name__ == '__main__':
    main()