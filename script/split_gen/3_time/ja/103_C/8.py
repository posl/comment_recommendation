def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    a.remove(max_a)
    a.append(max_a-1)
    print(sum(a))
