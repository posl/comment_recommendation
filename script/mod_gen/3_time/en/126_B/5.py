def main():
  S = input()
  s1 = S[0:2]
  s2 = S[2:4]
  if 1 <= int(s1) <= 12:
    if 1 <= int(s2) <= 12:
      print("AMBIGUOUS")
    else:
      print("MMYY")
  elif 1 <= int(s2) <= 12:
    print("YYMM")
  else:
    print("NA")

if __name__ == '__main__':
    main()