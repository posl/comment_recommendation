def main():
    n = int(input())
    n = str(n)
    if n[0] == n[1] and n[1] == n[2]:
        print(n)
    else:
        if n[0] == n[1]:
            if n[0] < n[2]:
                print(n[0] + n[1] + n[1])
            else:
                print(n[0] + n[0] + n[0])
        elif n[0] == n[2]:
            if n[0] < n[1]:
                print(n[0] + n[1] + n[0])
            else:
                print(n[0] + n[0] + n[0])
        else:
            if n[1] < n[2]:
                print(n[0] + n[1] + n[1])
            else:
                print(n[0] + n[0] + n[0])
