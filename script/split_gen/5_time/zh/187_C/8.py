def main():
  n = int(input())
  s = [input() for i in range(n)]
  s.sort()
  #print(s)
  for i in range(n):
    if s[i][0] != '!':
      if s[i][1:] in s:
        print(s[i][1:])
        exit()
