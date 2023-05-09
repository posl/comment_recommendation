def isSplit(s):
  if s[0] == '0':
    return 'No'
  if s[1] == '0' and s[2] == '0':
    return 'No'
  if s[7] == '0' and s[8] == '0' and s[9] == '0':
    return 'No'
  if s[3] == '0' and s[4] == '0' and s[5] == '0' and s[6] == '0':
    return 'No'
  return 'Yes'
