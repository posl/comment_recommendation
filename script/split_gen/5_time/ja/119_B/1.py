def main():
    n = int(input())
    x, u = [], []
    for i in range(n):
        x_i, u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)
    print(sum([x_i if u_i == "JPY" else x_i * 380000.0 for x_i, u_i in zip(x, u)]))
