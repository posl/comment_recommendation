def main():
    #input
    N = int(input())
    #compute
    if N%111 == 0:
        print(N)
    else:
        print(111*(N//111+1))
    #output

if __name__ == '__main__':
    main()