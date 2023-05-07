def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == "L":
            a.append(i+1)
        else:
            a.insert(-1,i+1)
    print(*a)
