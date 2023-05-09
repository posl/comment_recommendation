def main():
  x = input()
  n = int(input())
  s = []
  for i in range(n):
    s.append(input())
  s.sort(key=lambda s: [x.index(c) for c in s])
  for i in s:
    print(i)
