def main():
    n = input()
    n = list(n)
    n = list(map(int, n))
    s = sum(n)
    if s % 9 == 0:
        print("Yes")
    else:
        print("No")
