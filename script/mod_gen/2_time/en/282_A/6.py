def main():
    # get K
    k = int(input())
    
    # print out the answer
    print(''.join([chr(i) for i in range(65, 65 + k)]))
main()
