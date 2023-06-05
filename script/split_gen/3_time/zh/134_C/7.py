def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a_max = max(a)
    a_max_index = a.index(a_max)
    a.pop(a_max_index)
    for i in range(n-1):
        print(a_max)
