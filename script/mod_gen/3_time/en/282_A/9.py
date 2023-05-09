def main():
    #read the number of letters
    k = int(input())
    #print the first k uppercase letters in ascending order
    print(''.join([chr(i) for i in range(65,65+k)]))

if __name__ == '__main__':
    main()