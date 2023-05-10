def main():
    a_1, a_2, a_3 = map(int, input().split())
    if a_1 + a_2 + a_3 >= 22:
        print("bust")
    else:
        print("win")
