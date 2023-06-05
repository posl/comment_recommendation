def main():
    n = int(input())
    for_num = 0
    against_num = 0
    for i in range(n):
        s = input()
        if s == "For":
            for_num += 1
        elif s == "Against":
            against_num += 1
    if for_num > against_num:
        print("Yes")
    else:
        print("No")
main()
