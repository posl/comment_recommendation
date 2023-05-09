def main():
    k = int(input())
    s = input()
    n = len(s)
    if k >= n:
        print(s)
    else:
        print(s[:k] + "...")
