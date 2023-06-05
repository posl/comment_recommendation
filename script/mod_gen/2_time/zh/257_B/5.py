def get_char(n, x):
  a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  s = ""
  for i in range(1, n+1):
    s += a * n
  return s[x-1]

if __name__ == '__main__':
    get_char()