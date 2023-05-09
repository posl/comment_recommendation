def main():
  L, Q = map(int, input().split())
  arr = [0, L]
  for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
      arr.append(x)
    else:
      arr.sort()
      index = arr.index(x)
      print(arr[index] - arr[index - 1])
