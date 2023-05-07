def xor_sum(n, a):
  s = 0
  for i in range(n-1):
    for j in range(i+1, n):
      s += a[i] ^ a[j]
  return s % (10**9+7)

if __name__ == '__main__':
    xor_sum()