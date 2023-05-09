def  main():
    N =  int (input())
    A = [ int (a)  for  a  in  input().split()]
    A = [0] + A + [0]
    ans = 0 
    for  i  in  range(1, N + 2):
        ans +=  max (A[i - 1], A[i])
    print(ans)
