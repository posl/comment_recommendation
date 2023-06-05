def main():
    n = int(input())
    list = []
    for i in range(n):
        s, t = input().split()
        list.append(s + t)
    if len(list) == len(set(list)):
        print("No")
    else:
        print("Yes")
main()
