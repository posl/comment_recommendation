def main():
  s1 = input()
  s2 = input()
  if s1.count('#') >= 2 or s2.count('#') >= 2:
    print('Yes')
  else:
    print('No')
