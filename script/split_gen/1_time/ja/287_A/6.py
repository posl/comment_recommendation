def main():
    n = int(input())
    list = []
    for i in range(n):
        list.append(input())
    if list.count("For") > n/2:
        print("Yes")
    else:
        print("No")
main()
