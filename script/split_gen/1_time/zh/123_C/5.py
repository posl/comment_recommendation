def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min = n
    if min > a:
        min = a
    if min > b:
        min = b
    if min > c:
        min = c
    if min > d:
        min = d
    if min > e:
        min = e
    if min == n:
        print(5)
    elif n % min == 0:
        print(n // min + 4)
    else:
        print(n // min + 5)
