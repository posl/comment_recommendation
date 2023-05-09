def main():
    N = int(input())
    #print(N)
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            j = N//i
            #print(j, i)
    print(j+i-2)

if __name__ == '__main__':
    main()