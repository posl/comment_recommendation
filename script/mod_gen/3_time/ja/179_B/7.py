def main():
  N = int(input())
  D = []
  for i in range(N):
    D.append(list(map(int, input().split())))
  count = 0
  for i in range(N):
    if D[i][0] == D[i][1]:
      count += 1
    else:
      count = 0
    if count >= 3:
      print("Yes")
      return
  print("No")

if __name__ == '__main__':
    main()