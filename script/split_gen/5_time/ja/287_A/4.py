def main():
    n = int(input())
    s = [input() for i in range(n)]
    if s.count("For") > n/2:
        print("Yes")
    else:
        print("No")
