def main():
    n = int(input())
    s = input()
    flag = False
    for i in range(1, n):
        if s[:i] == s[i:]:
            flag = True
            break
    if flag:
        print("Yes")
    else:
        print("No")
