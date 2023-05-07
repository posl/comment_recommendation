def main():
    #input
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    #compute
    #output
    print(H.index(min(H, key=lambda x: abs(A-T+0.006*x)))+1)

if __name__ == '__main__':
    main()