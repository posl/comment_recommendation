def check(ary, p):
  for i in range(len(ary)):
    if ary[i] % 2 != p[i]:
      return False
  return True
