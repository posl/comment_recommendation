def main():
  N, K = map(int, input().split())
  friends = []
  for i in range(N):
    A, B = map(int, input().split())
    friends.append((A, B))
  friends.sort()
  for friend in friends:
    if friend[0] > K:
      break
    K += friend[1]
  print(K)
