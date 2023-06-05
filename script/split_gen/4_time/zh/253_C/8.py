def main():
    n = int(input())
    for i in range(n):
        a = input().split()
        if a[0] == "1":
            print("insert")
        elif a[0] == "2":
            print("delete")
        else:
            print("print")
