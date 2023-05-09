def main():
    #read input
    A, B, C = map(int, input().split())
    #swap A and B
    A, B = B, A
    #swap A and C
    A, C = C, A
    #print output
    print(A, B, C)
main()

if __name__ == '__main__':
    main()