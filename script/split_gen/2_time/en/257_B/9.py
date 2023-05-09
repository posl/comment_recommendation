def main():
    #read input
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    
    #make a list of pieces
    pieces = [0] * n
    for i in range(k):
        pieces[a[i] - 1] = i + 1
    
    #process operations
    for i in range(q):
        #if the piece is on the rightmost square, do nothing
        if pieces[l[i] - 1] == 0:
            continue
        #if the piece is not on the rightmost square, move it one square right if there is no piece on the next square on the right
        else:
            #if the piece is on the rightmost square, do nothing
            if l[i] == n:
                continue
            #if the piece is not on the rightmost square, move it one square right if there is no piece on the next square on the right
            else:
                #if there is no piece on the next square on the right, move the piece one square right
                if pieces[l[i]] == 0:
                    pieces[l[i]] = pieces[l[i] - 1]
                    pieces[l[i] - 1] = 0
                #if there is a piece on the next square on the right, do nothing
                else:
                    continue
    
    #print the index of the square on which the i-th piece from the left is after the Q operations have ended
    for i in range(k):
        print(pieces.index(i + 1) + 1, end = " ")
