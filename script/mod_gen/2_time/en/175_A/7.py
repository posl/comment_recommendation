def main():
  S = input()
  cnt = 0
  max_cnt = 0
  for i in S:
    if i == "R":
      cnt += 1
    else:
      if max_cnt < cnt:
        max_cnt = cnt
      cnt = 0
  if max_cnt < cnt:
    max_cnt = cnt
  print(max_cnt)

if __name__ == '__main__':
    main()