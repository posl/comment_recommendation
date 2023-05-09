def main():
    # get K
    k = int(input())
    
    # print out the answer
    print(''.join([chr(i) for i in range(65, 65 + k)]))
main()

if __name__ == '__main__':
    main()