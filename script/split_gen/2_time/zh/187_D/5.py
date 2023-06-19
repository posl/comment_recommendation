def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a.append(int(input().split()[0]))
        b.append(int(input().split()[1]))
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum > b_sum:
        print(0)
    else:
        a_b = [i for i in range(n)]
        for i in range(n):
            a_b[i] = a[i] - b[i]
        a_b.sort()
        a_b.reverse()
        a_b_sum = 0
        for i in range(n):
            a_b_sum += a_b[i]
            if a_b_sum + a_sum > b_sum:
                print(i+1)
                break
