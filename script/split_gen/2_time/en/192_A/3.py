def main():
    x = int(input())
    if x%100 == 0:
        print(0)
    else:
        print(100 - (x%100))
