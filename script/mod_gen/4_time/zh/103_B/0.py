def main():
  s = input()
  t = input()
  if s == t:
    print("Yes")
  else:
    for i in range(len(s)):
      s = s[-1] + s[:-1]
      if s == t:
        print("Yes")
        break
      elif i == len(s) - 1:
        print("No")
        break

if __name__ == '__main__':
    main()