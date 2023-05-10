def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a_set = set(a)
    b_set = set(b)
    a_b_set = a_set | b_set
    if len(a_b_set) == n:
        print("Yes")
    else:
        print("No")
