def problem164_a():
    s,w = map(int, input().split())
    if w >= s:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    problem164_a()