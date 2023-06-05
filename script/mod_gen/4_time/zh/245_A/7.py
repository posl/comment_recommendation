def main():
    A, B, C, D = map(int, input().split())
    t1 = A * 60 + B
    t2 = C * 60 + D
    if t1 < t2:
        print("青木")
    else:
        print("高桥")
main()
