def shift_string(s, n):
  s = s.upper()
  if n == 0:
    return s
  else:
    result = ''
    for c in s:
      result += chr(((ord(c) - 65 + n) % 26) + 65)
    return result

if __name__ == '__main__':
    shift_string()