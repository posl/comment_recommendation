def main():
  n, m = map(int, input().split())
  a = [input() for _ in range(2*n)]
  rank = [0] * (2*n)
  for i in range(2*n):
    rank[i] = (0, i+1)
  for i in range(m):
    rank.sort()
    new_rank = []
    for j in range(n):
      p1 = rank[2*j][1] - 1
      p2 = rank[2*j+1][1] - 1
      if a[p1][i] == a[p2][i]:
        new_rank.append(rank[2*j])
        new_rank.append(rank[2*j+1])
      elif a[p1][i] == 'G' and a[p2][i] == 'C':
        new_rank.append((rank[2*j][0]+1, rank[2*j][1]))
        new_rank.append(rank[2*j+1])
      elif a[p1][i] == 'C' and a[p2][i] == 'P':
        new_rank.append((rank[2*j][0]+1, rank[2*j][1]))
        new_rank.append(rank[2*j+1])
      elif a[p1][i] == 'P' and a[p2][i] == 'G':
        new_rank.append((rank[2*j][0]+1, rank[2*j][1]))
        new_rank.append(rank[2*j+1])
      else:
        new_rank.append(rank[2*j])
        new_rank.append((rank[2*j+1][0]+1, rank[2*j+1][1]))
    rank = new_rank
  rank.sort()
  for i in range(2*n):
    print(rank[i][1])

if __name__ == '__main__':
    main()