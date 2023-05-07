def main():
    string = input()
    length = len(string)
    if string == string[::-1]:
        if string[:int((length-1)/2)] == string[:int((length-1)/2):-1]:
            if string[int((length+3)/2)-1:] == string[int((length+3)/2)-1::-1]:
                print("Yes")
                exit()
    print("No")
main()

if __name__ == '__main__':
    main()