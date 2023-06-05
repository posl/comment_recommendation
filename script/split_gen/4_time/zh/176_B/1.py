def main():
    n = input()
    n = list(n)
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")
