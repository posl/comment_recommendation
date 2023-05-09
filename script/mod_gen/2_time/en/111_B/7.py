def main():
    #input
    N = int(input())
    #output
    print(N//111*111+111 if N%111!=0 else N)

if __name__ == '__main__':
    main()