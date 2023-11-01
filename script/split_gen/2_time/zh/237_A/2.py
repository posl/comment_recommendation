def main():
    n = int(input())
    if n >= -2**31 and n <= 2**31-1:
        print("Yes")
    else:
