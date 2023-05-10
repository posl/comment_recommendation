def main():
    N = input()
    n = 0
    for i in N:
        n += int(i)
    if n % 9 == 0:
        print("Yes")
    else:
        print("No")
