def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()
    if S_1 == S_2 or S_1 == S_3 or S_1 == S_4 or S_2 == S_3 or S_2 == S_4 or S_3 == S_4:
        print("No")
    else:
        print("Yes")
