def get_good_ints(N, W, A):
    A.sort()
    #print(A)
    #print(N, W, A)
    if A[0] > W:
        return 0
    if A[0] == 1:
        return W
    if A[0] == 2:
        return W//2 + W%2
    if A[0] == 3:
        return W//3 + W%3
    if A[0] == 4:
        return W//4 + W%4
    if A[0] == 5:
        return W//5 + W%5
    if A[0] == 6:
        return W//6 + W%6
    if A[0] == 7:
        return W//7 + W%7
    if A[0] == 8:
        return W//8 + W%8
    if A[0] == 9:
        return W//9 + W%9
    if A[0] == 10:
        return W//10 + W%10
    if A[0] == 11:
        return W//11 + W%11
    if A[0] == 12:
        return W//12 + W%12
    if A[0] == 13:
        return W//13 + W%13
    if A[0] == 14:
        return W//14 + W%14
    if A[0] == 15:
        return W//15 + W%15
    if A[0] == 16:
        return W//16 + W%16
    if A[0] == 17:
        return W//17 + W%17
    if A[0] == 18:
        return W//18 + W%18
    if A[0] == 19:
        return W//19 + W%19
    if A[0] == 20:
        return W//20 + W%20
    if A[0] == 21:
        return W//21 + W%21
    if A[0] == 22:
        return W//22 + W%22
    if A[0] == 23:
        return W//23 + W%23
    if A[

if __name__ == '__main__':
    get_good_ints()