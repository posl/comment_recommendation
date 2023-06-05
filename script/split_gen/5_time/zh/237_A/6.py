def main():
    n = int(input())
    if -2**31 <= n and n <= 2**31-1:
        print("是")
    else:
        print("否")
