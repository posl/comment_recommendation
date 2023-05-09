def main():
  n = int(input())
  s = []
  d = {}
  for i in range(n):
    s.append(input())
  for i in range(n):
    if s[i] in d:
      d[s[i]] += 1
      print(s[i] + "(" + str(d[s[i]]) + ")")
    else:
      d[s[i]] = 0
      print(s[i])
main()

if __name__ == '__main__':
    main()