def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    max_a_idx = a.index(max_a)
    a.pop(max_a_idx)
    max_a2 = max(a)
    for i in range(n):
        if i == max_a_idx:
            print(max_a2)
        else:
            print(max_a)
