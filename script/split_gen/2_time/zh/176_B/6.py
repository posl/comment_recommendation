def main():
    n = input()
    n = list(n)
    n = list(map(int, n))
    sum = 0
    for i in n:
        sum += i
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")
