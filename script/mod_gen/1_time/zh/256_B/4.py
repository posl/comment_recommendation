def baseball_game(N, A):
    P = 0
    for i in range(N):
        #print('i=', i)
        #print('P=', P)
        #print('A[i]=', A[i])
        #print('A=', A)
        if i == 0:
            A[0] += 1
        else:
            A[0] += 1
            for j in range(i):
                if A[j] + A[i] > 4:
                    P += 1
                    A[j] = 0
                else:
                    A[j] += A[i]
        #print('A=', A)
        #print('P=', P)
        #print('------------------')
    print(P)
    return P

if __name__ == '__main__':
    baseball_game()