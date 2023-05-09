def main():
    N = int(input())
    print( (N//2)/N if N%2 == 0 else ((N//2)+1)/N )

if __name__ == '__main__':
    main()