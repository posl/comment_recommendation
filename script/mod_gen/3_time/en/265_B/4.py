def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    #print(N, M, T, A, X, Y)
    #Takahashi starts with T seconds.
    #He can move from Room i to Room i+1 in A[i] seconds.
    #There are M bonus rooms.
    #When he reaches Room X[i], the time limit increases by Y[i] seconds.
    #Can he reach Room N?
    #We have to check whether he can reach Room N with time T.
    #If he can reach Room N with time T, then he can reach Room N with time T+Y[i] for any bonus room i.
    #So, we can check whether he can reach Room N with time T+Y[i] for any bonus room i.
    #We can check this by simulating the process.
    #We start with Room 1 and time T.
    #We move to Room 2 in A[0] seconds.
    #If the time is less than X[0], then we can move to Room 3 in A[1] seconds.
    #If the time is less than X[1], then we can move to Room 4 in A[2] seconds.
    #If the time is less than X[2], then we can move to Room 5 in A[3] seconds.
    #If the time is less than X[3], then we can move to Room 6 in A[4] seconds.
    #If the time is less than X[4], then we can move to Room 7 in A[5] seconds.
    #If the time is less than X[5], then we can move to Room 8 in A[6] seconds.
    #If the time is less than X[6], then we can move to Room 9 in A[7] seconds.
    #If the time is less than X[7], then we can move to Room 10 in A[8] seconds.
    #If the time is less than X[8], then we can move to Room 11 in A[9] seconds.

if __name__ == '__main__':
    main()