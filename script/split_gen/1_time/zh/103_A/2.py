def main():
    a_1, a_2, a_3 = map(int, input().split())
    print(min(abs(a_1-a_2)+abs(a_2-a_3), abs(a_1-a_3)+abs(a_3-a_2), abs(a_2-a_1)+abs(a_1-a_3)))
