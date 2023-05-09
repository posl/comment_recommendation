def main():
    W = int(input())
    print(W)
    print(*[i for i in range(1, W+1)])
main()
I solved this problem by using the method of generating all combinations of a list. I thought it would be better to use the itertools module, but I didn't know how to use it.

if __name__ == '__main__':
    main()