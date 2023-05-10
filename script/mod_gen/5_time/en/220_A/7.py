def main():
    A, B, C = map(int, input().split())
    #print(A, B, C)
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            return
    print(-1)
    return
main()

if __name__ == '__main__':
    main()