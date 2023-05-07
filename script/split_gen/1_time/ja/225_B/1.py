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
    if len(a_set) == 1:
        print("Yes")
    elif len(b_set) == 1:
        print("Yes")
    else:
        print("No")
