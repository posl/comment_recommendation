def median():
    a,b,c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print("Yes")
    else:
        print("No")
median()

if __name__ == '__main__':
    median()