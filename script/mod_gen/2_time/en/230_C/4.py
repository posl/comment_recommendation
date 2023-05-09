def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    #print(N, A, B)
    #print(P, Q, R, S)
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i+j) % 2 == (A+B) % 2:
                print('#', end = '')
            else:
                print('.', end = '')
        print()

if __name__ == '__main__':
    main()