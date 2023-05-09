def main():
    #input
    A, B = map(int, input().split())
    #compute
    for i in range(1, 1001):
        if A == i//1.08 and B == i//1.1:
            print(i)
            break
    else:
        print(-1)
    #output

if __name__ == '__main__':
    main()