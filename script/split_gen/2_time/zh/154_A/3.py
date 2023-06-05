def solve(h):
  if h == 1:
    return 1
  elif h % 2 == 0:
    return solve(h//2) * 2 + 1
  else:
    return solve(h//2) * 2 + 1
print(solve(int(input())))
