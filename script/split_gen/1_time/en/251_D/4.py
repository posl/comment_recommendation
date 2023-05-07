def main():
    W = int(input())
    if W <= 2:
        print("NO")
    else:
        if W % 2 == 0:
            print("YES")
        else:
            print("NO")
