def main():
    n = int(input())
    result = []
    for i in range(n):
        result.append(input())
    if result.count("For") > n//2:
        print("Yes")
    else:
        print("No")
