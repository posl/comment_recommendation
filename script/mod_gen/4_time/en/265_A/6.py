def main():
  X,Y,N = map(int,input().split())
  if N%3==0:
    print(N/3*Y)
  elif N%3==1:
    print((N-1)/3*Y+X)
  else:
    print((N-2)/3*Y+2*X)

if __name__ == '__main__':
    main()