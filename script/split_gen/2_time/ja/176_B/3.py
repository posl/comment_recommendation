def main():
    n = input()
    n = list(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum%9 == 0:
        print("Yes")
    else:
        print("No")
