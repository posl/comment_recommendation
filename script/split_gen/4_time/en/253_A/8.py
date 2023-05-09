def main():
    a = input()
    b = input()
    c = input()
    if(b > a and b < c) or (b > c and b < a):
        print("Yes")
    else:
        print("No")
