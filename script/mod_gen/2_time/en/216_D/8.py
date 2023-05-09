def isPossible(N,M,K,A):
    from collections import Counter
    #print("M,K,A",M,K,A)
    if M==2:
        if K[0]==K[1]:
            if Counter(A[0])==Counter(A[1]):
                return True
    return False

if __name__ == '__main__':
    isPossible()