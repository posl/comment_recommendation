def main():
    #input
    N, A, B = map(int, input().split())
    #calc
    #output
    print(min(A*N, B))

if __name__ == '__main__':
    main()