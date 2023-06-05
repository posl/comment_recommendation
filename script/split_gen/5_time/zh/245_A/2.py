def main():
    a, b, c, d = map(int, input().split())
    time_a = a*60 + b
    time_b = c*60 + d
    if time_a < time_b:
        print("高桥")
    else:
        print("青木")
