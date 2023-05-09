def main():
  H, W = map(int, input().split())
  C = [input() for i in range(H)]
  for i in range(W):
    count = 0
    for j in range(H):
      if C[j][i] == '#':
        count += 1
    print(count, end=' ')

if __name__ == '__main__':
    main()