def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_num = max(a)
    max_num = min(b)
    print(max_num - min_num + 1 if max_num >= min_num else 0)
