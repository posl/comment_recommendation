def is_odd(n):
  return n % 2 == 1
s = input()
s = list(s)
odd = s[::2]
even = s[1::2]

if __name__ == '__main__':
    is_odd()