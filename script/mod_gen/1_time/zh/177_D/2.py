def find(x):
  if x == parents[x]:
    return x
  else:
    parents[x] = find(parents[x])
    return parents[x]

if __name__ == '__main__':
    find()