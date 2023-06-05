def main():
  N, A, B = [int(x) for x in input().split()]
  P, Q, R, S = [int(x) for x in input().split()]
  
  #print(N, A, B)
  #print(P, Q, R, S)
  
  #print("N:", N)
  #print("A:", A)
  #print("B:", B)
  #print("P:", P)
  #print("Q:", Q)
  #print("R:", R)
  #print("S:", S)
  
  #print("max(1-A,1-B):", max(1-A,1-B))
  #print("min(N-A,N-B):", min(N-A,N-B))
  #print("max(1-A,B-N):", max(1-A,B-N))
  #print("min(N-A,B-1):", min(N-A,B-1))
  
  #print("P+i-1:", P+i-1)
  #print("R+j-1:", R+j-1)
  
  for i in range(P, Q+1):
    for j in range(R, S+1):
      if (max(1-A,1-B) <= i <= min(N-A,N-B)) and (A+i, B+i) == (i, j):
        print("#", end="")
      elif (max(1-A,B-N) <= i <= min(N-A,B-1)) and (A+i, B-i) == (i, j):
        print("#", end="")
      else:
        print(".", end="")
    print()

if __name__ == '__main__':
    main()