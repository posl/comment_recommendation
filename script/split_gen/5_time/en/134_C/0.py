def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max_a = max(a)
    max_a_index = a.index(max_a)
    for i in range(n):
        if i == max_a_index:
            print(sorted(a, reverse=True)[1])
        else:
            print(max_a)
