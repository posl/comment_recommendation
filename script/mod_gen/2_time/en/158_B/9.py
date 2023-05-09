def main():
    #input
    N, A, B = map(int, input().split())
    #compute
    #output
    print(min(N//A*B + min(N%A, B), N))
main()

if __name__ == '__main__':
    main()