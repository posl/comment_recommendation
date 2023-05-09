def main():
  N, M = map(int, input().split())
  L = []
  for i in range(M):
    L.append(list(map(int, input().split())))
  #print(L)
  if M == 0:
    if N == 1:
      print(0)
    else:
      print(10**(N-1))
    return
  for i in range(10**(N-1), 10**N):
    i = str(i)
    for j in range(M):
      if int(i[L[j][0]-1]) != L[j][1]:
        break
    else:
      print(i)
      return
  print(-1)

if __name__ == '__main__':
    main()