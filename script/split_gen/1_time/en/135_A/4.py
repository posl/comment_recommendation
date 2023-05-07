def main():
    A, B = [int(x) for x in input().split()]
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print("IMPOSSIBLE")
