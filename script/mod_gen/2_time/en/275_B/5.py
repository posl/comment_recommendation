def main():
  A,B,C,D,E,F = map(int,input().split())
  print((A*B*C-D*E*F)%998244353)
main()
I'm not sure about the constraints, but I think the constraints are not necessary.

if __name__ == '__main__':
    main()