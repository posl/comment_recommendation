def main():
    n = int(input())
    for i in range(1,10):
        if n % i == 0:
            if n // i < 10:
                print("Yes")
                return
    print("No")
