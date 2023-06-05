def main():
    n = input()
    total = 0
    for i in range(len(n)):
        total += int(n[i])
    if total % 9 == 0:
        print("Yes")
    else:
        print("No")
