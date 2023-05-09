def main():
    a = input().split()
    a = [int(x) for x in a]
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")
