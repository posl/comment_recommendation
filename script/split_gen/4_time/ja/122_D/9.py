def check(s):
  if s.count("AGC") >= 1:
    return False
  for i in range(len(s)-1):
    if s[i:i+2] == "AGC":
      return False
    if i+3 < len(s):
      if s[i:i+3] == "AGC":
        return False
  return True
