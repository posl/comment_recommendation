def main():
    n,c = map(int, input().split())
    a = []
    b = []
    cost = []
    for i in range(n):
        a_i, b_i, c_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        cost.append(c_i)
    print(n,c)
    print(a)
    print(b)
    print(cost)
    print("end")
