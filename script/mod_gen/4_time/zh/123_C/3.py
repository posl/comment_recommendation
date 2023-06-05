def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min = 0
    if a < b:
        min = a
    else:
        min = b
    if min > c:
        min = c
    if min > d:
        min = d
    if min > e:
        min = e
    if n % min == 0:
        print(n // min + 4)
    else:
        print(n // min + 5)
main()
