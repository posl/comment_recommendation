def main():
    a = [int(i) for i in input().split()]
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")
