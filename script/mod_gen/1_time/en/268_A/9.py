def main():
    #Read input
    input_list = input().split()
    #Convert input to integers
    int_list = [int(i) for i in input_list]
    #Convert to set to remove duplicates
    int_set = set(int_list)
    #Print length of set
    print(len(int_set))

if __name__ == '__main__':
    main()