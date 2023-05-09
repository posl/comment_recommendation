Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    ans = ''
    for s in S:
        if ord(s) + N > 90:
            ans += chr(ord(s) + N - 26)
        else:
            ans += chr(ord(s) + N)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    ans = ''
    for i in range(len(S)):
        ans += chr((ord(S[i]) - ord('A') + N) % 26 + ord('A'))
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for c in s:
        result += alphabet[(alphabet.index(c) + n) % 26]
    print(result)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    l = len(s)
    result = ""
    for i in range(l):
        result += chr((ord(s[i]) - 65 + n) % 26 + 65)
    print(result)

=======
Suggestion 5

def rotate(s, n):
    result = ""
    for c in s:
        if c.isalpha():
            if c.isupper():
                result += chr((ord(c) - 65 + n) % 26 + 65)
            else:
                result += chr((ord(c) - 97 + n) % 26 + 97)
        else:
            result += c
    return result

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabets = alphabets * 2
    result = ""
    for i in range(len(S)):
        index = alphabets.find(S[i])
        result += alphabets[index + N]
    print(result)

=======
Suggestion 7

def shift(s, n):
    s = s.upper()
    result = ""
    for c in s:
        if c.isalpha():
            if ord(c) + n > ord('Z'):
                result += chr(ord(c) + n - ord('Z') + ord('A') - 1)
            else:
                result += chr(ord(c) + n)
        else:
            result += c
    return result

=======
Suggestion 8

def main():
    n = int(input())
    s = input()

    #print(n)
    #print(s)

    l = list(s)
    #print(l)

    for i in range(len(l)):
        l[i] = ord(l[i]) + n
        #print(l[i])

        if l[i] > ord('Z'):
            l[i] = l[i] - ord('Z') + ord('A') - 1

        l[i] = chr(l[i])
        #print(l[i])

    print(''.join(l))

=======
Suggestion 9

def shift_string(s, n):
    # string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    # string.digits = '0123456789'
    # string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    # string.printable = string.digits + string.ascii_letters + string.punctuation + ' '
    # string.whitespace = ' \t\n\r\x0b\x0c'
    # string.capwords(s) = Capitalize the words in s, and return the result.
    # string.capwords(s, sep) = Capitalize the words in s, and return the result, as a string.
    # string.capwords(s, None) = Capitalize the words in s, and return the result, as a string.
    # string.capwords(s, sep=None) = Capitalize the words in s, and return the result, as a string.
    # string.capwords(s, sep=None, lowercase=False) = Capitalize the words in s, and return the result, as a string.
    # string.capwords(s, sep=None, lowercase=True) = Capitalize the words in s, and return the result, as a string.
    # string.capwords(s, sep=None, lowercase=True, keepends=False) = Capitalize the words in s, and return the result, as a string.
    # string.capwords(s, sep=None, lowercase=True, keepends=True) = Capitalize the words in s, and return the result, as a string.
    # string.capwords(s, sep=None, lowercase=False, keepends=False) = Capitalize the words in s, and return the result, as a string.
    # string.capwords(s, sep=None, lowercase=False, keepends=True) = Capitalize the words in s, and return the result, as a string.
    # string.capwords(s, sep=None, lowercase=False, keepends=False, preserve=False) = Capitalize the words in s, and return the result, as a string.
    # string.capwords(s, sep=None, lowercase=False, keepends=True, preserve=False) = Capitalize the words in s, and return the result, as a string.
    # string.capwords(s, sep=None, lowercase=False, keepends=False, preserve=True) = Capitalize the words in s

=======
Suggestion 10

def shift_string(s, n):
  s = s.upper()
  if n == 0:
    return s
  else:
    result = ''
    for c in s:
      result += chr(((ord(c) - 65 + n) % 26) + 65)
    return result
