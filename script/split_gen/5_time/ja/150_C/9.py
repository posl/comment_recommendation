def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p_index = 0
    q_index = 0
    for i in range(n):
        p_index += (p[i] - 1) * math.factorial(n - i - 1)
        q_index += (q[i] - 1) * math.factorial(n - i - 1)
    print(abs(p_index - q_index))
