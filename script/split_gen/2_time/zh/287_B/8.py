def main():
    n = int(input())
    for_count = 0
    against_count = 0
    for i in range(n):
        s = input()
        if s == "For":
            for_count += 1
        else:
            against_count += 1
    if for_count > against_count:
        print("Yes")
    else:
        print("No")
