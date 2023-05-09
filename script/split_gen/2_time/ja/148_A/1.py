def main():
    a = int(input())
    b = int(input())
    c = 0
    for i in range(1,4):
        if i != a and i != b:
            c = i
    print(c)
