def check_condition(n, a):
  for i in range(n):
    if a[i] % 2 == 0 and (a[i] % 3 != 0 and a[i] % 5 != 0):
      return False
  return True

if __name__ == '__main__':
    check_condition()