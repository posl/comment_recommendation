def  main():
    N, M, K =  map ( int ,  input (). split ())
    A = []
    B = []
    C = []
    D = []
     for  i  in   range (M):
        a, b =  map ( int ,  input (). split ())
        A.append(a)
        B.append(b)
     for  i  in   range (K):
        c, d =  map ( int ,  input (). split ())
        C.append(c)
        D.append(d)
    friends =  dict ()
     for  i  in   range (N):
        friends[i + 1] = []
     for  i  in   range (M):
        friends[A[i]].append(B[i])
        friends[B[i]].append(A[i])
    blocks =  dict ()
     for  i  in   range (N):
        blocks[i + 1] = []
     for  i  in   range (K):
        blocks[C[i]].append(D[i])
        blocks[D[i]].append(C[i])
    ans =  [0] * N
     for  i  in   range (N):
        ans[i] =  len (friends[i + 1]) +  len (blocks[i + 1])
        ans[i] = N - ans[i] - 1
         for  j  in  friends[i + 1]:
            ans[j - 1] -= 1
             if  i + 1  in  blocks[j]:
                ans[j - 1] += 1
     for  i  in  ans:
        print (i,  end = ' ' )
    print ()

if __name__ == '__main__':
    ()