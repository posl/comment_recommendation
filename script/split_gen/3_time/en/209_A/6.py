def main():
    # put your code here
    a, b = map(int, input().split())
    if a > b:
        print(0)
    else:
        print(b - a + 1)
