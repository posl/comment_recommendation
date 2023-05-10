def problem100_a():
    a,b = map(int,input().split())
    if a > 8 or b > 8:
        print(":(")
    else:
        print("Yay!")

if __name__ == '__main__':
    problem100_a()