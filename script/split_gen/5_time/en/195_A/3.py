def main():
    m, h = input().split()
    if int(h) % int(m) == 0:
        print("Yes")
    else:
        print("No")
