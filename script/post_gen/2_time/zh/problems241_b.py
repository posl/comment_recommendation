Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = raw_input().split()
    b = [0]*10
    for i in range(10):
        b[i] = int(a[i])
    for j in range(3):
        b[0] = b[b[0]]
    print b[0]

=======
Suggestion 2

def main():
    a = [int(x) for x in input().split()]
    n = 0
    for i in range(10):
        n = a[n]
    print(n)

=======
Suggestion 3

def get_next_number(k, a):
    return a[k]

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 5

def get_next_number(n):
    return a[n]

a = [int(i) for i in input().split()]
n = 0
for i in range(3):
    n = get_next_number(n)
print(n)

=======
Suggestion 6

def read_ints():
    return list(map(int, input().split()))

=======
Suggestion 7

def main():
    a = list(map(int, input().split()))
    for i in range(10):
        if a[0] == a[i]:
            print(i)
            break

=======
Suggestion 8

def main():
    a = list(map(int, input().split()))
    b = [0]
    for i in range(100):
        b.append(a[b[-1]])
    print(b[3])

=======
Suggestion 9

def get_a_k(a, k):
    return a[k]
