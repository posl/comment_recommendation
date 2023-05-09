def main():
    #input
    k = int(input())
    #output
    print(''.join([chr(i) for i in range(65,65+k)]))

if __name__ == '__main__':
    main()