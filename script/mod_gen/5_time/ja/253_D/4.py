def main():
    N,A,B = map(int,input().split())
    #print(N,A,B)
    #print(N//A)
    #print(N//B)
    #print(N//(A*B))
    print(N-(N//A+N//B-N//(A*B))*2)
    return

if __name__ == '__main__':
    main()