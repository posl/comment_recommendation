def main():
    input_str = input()
    input_list = input_str.split()
    D = int(input_list[0])
    N = int(input_list[1])
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(N*100)
    else:
        if N == 100:
            print(1010000)
        else:
            print(N*10000)

if __name__ == '__main__':
    main()