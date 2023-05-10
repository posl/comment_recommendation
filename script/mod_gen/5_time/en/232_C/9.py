def check_shape(N, M, Takahashi, Aoki):
    #print("Takahashi: ", Takahashi)
    #print("Aoki: ", Aoki)
    for i in range(N):
        for j in range(N):
            if Takahashi[i][j] != Aoki[i][j]:
                return False
    return True

if __name__ == '__main__':
    check_shape()