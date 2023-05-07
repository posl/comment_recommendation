def get_good_integers(W, A):
    A = sorted(A)
    #print(A)
    good_integers = set()
    for i in range(2**len(A)):
        #print("i=", i)
        total = 0
        for j in range(len(A)):
            #print("j=", j)
            if i & (1<<j):
                #print("i=", i, "j=", j)
                total += A[j]
                #print("total=", total)
        if total <= W:
            good_integers.add(total)
    return len(good_integers)

if __name__ == '__main__':
    get_good_integers()