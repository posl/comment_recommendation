def main():
    N = int(input())
    if N < 250:
        print(0)
        return
    if N < 1000:
        print(1)
        return
    if N < 1000000:
        print(2)
        return
    if N < 1000000000:
        print(3)
        return
    if N < 1000000000000:
        print(4)
        return
    if N < 1000000000000000:
        print(5)
        return
    print(6)
