def main():
    input = raw_input().split()
    A = int(input[0])
    B = int(input[1])
    C = int(input[2])
    
    for i in range(A, B+1):
        if i%C == 0:
            print i
            return
    print -1

if __name__ == '__main__':
    main()