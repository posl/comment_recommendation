Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def sequence(n):
    if n == 1:
        return "1"
    else:
        return sequence(n-1) + " " + str(n) + " " + sequence(n-1)

=======
Suggestion 2

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

n = int(input())
print(*s(n))

=======
Suggestion 3

def main():
    n = int(input())
    s = '1'
    for i in range(2, n+1):
        s = s + ' ' + str(i) + ' ' + s
    print(s)

=======
Suggestion 4

def sequence(n):
    if n == 1:
        return [1]
    else:
        return sequence(n-1) + [n] + sequence(n-1)

n = int(input())
print(*sequence(n))

=======
Suggestion 5

def main():
    n = int(input())
    s = "1"
    for i in range(1, n):
        s = s + " " + str(i+1) + " " + s
    print(s)

=======
Suggestion 6

def s(n):
  if n == 1:
    return [1]
  else:
    return s(n-1) + [n] + s(n-1)

print(" ".join(map(str, s(int(input())))))

=======
Suggestion 7

def getSequence(n):
    if n == 1:
        return [1]
    else:
        seq = getSequence(n-1)
        return seq + [n] + seq

=======
Suggestion 8

def print_sequence(n):
    if n == 1:
        return [1]
    else:
        seq = print_sequence(n-1)
        return seq + [n] + seq

=======
Suggestion 9

def concat(seq, n):
    if n == 1:
        return seq
    else:
        return concat(seq, n-1) + [n] + seq
