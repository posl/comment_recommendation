def main():
  #N, M = map(int, input().split())
  #A = list(map(int, input().split()))
  N, M = 3, 2
  A = [380, 19, 1]
  #N, M = 12, 3
  #A = [4, 56, 78, 901, 2, 345, 67, 890, 123, 45, 6, 789]
  A.sort(reverse=True)
  if A[M-1] >= sum(A)*1/(4*M):
    print('Yes')
  else:
    print('No')
main()

if __name__ == '__main__':
    main()