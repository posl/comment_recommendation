def is_polygon(L):
  n = len(L)
  if n < 3:
    return False
  L.sort()
  return L[-1] < sum(L[:-1])
