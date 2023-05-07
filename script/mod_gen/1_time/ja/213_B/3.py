def main():
  n = int(input())
  a = list(map(int,input().split()))
  b = sorted(a)
  print(a.index(b[1])+1)
main()

if __name__ == '__main__':
    main()