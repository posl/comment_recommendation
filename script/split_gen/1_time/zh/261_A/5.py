def main():
    l_1, r_1, l_2, r_2 = map(int, input().split())
    if l_2 > r_1 or l_1 > r_2:
        print(0)
    elif l_1 <= l_2 and r_1 <= r_2:
        print(r_1 - l_2)
    elif l_2 <= l_1 and r_2 <= r_1:
        print(r_2 - l_1)
    elif l_1 <= l_2 and r_2 <= r_1:
        print(r_2 - l_2)
    elif l_2 <= l_1 and r_1 <= r_2:
        print(r_1 - l_1)
    else:
        print(0)
