def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    #print(N, A, B)
    #print(P, Q, R, S)
    #print("max(1-A,1-B)≦ k≦ min(N-A,N-B)")
    #print("max(1-A,B-N)≦ k≦ min(N-A,B-1)")
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i >= A and j >= B) or (i >= B and j >= A):
                print("#", end="")
            else:
                print(".", end="")
        print("")

if __name__ == '__main__':
    main()