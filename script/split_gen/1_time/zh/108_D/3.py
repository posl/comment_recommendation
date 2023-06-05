def main():
    l = int(input())
    print(2*(l-1)+1, 2*(l-1)+l)
    for i in range(l-1):
        print(i+1, i+2, 0)
        print(i+1, i+2, 1)
    for i in range(l-1):
        print(i+1, i+2, l-1-i)
    for i in range(l-2):
        print(i+1, i+3, l-1-i)
    print(1, l, l-1)
