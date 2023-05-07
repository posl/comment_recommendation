def main():
    #input
    T = int(input())
    for i in range(T):
        N = int(input())
        A = [int(x) for x in input().split()]
        #count odd numbers
        count = 0
        for x in A:
            if x % 2 == 1:
                count = count + 1
        #output
        print(count)
main()

if __name__ == '__main__':
    main()