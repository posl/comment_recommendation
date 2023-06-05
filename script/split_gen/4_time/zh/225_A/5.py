def main():
    s = input()
    count = 0
    for i in range(3):
        if s[i] == "a":
            count += 1
    if count == 1:
        print(1)
    elif count == 2:
        print(3)
    elif count == 3:
        print(6)
