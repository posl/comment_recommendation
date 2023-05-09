def rec(i, m, n, a):
  if i == n:
    print(' '.join(map(str, a)))
    return
  for j in range(1, m+1):
    a[i] = j
    rec(i+1, m, n, a)

if __name__ == '__main__':
    rec()