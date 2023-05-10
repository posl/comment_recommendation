def find(x):
  if par[x] < 0:
    return x
  else:
    par[x] = find(par[x])
    return par[x]
