def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_mod = [a % 200 for a in A]
    A_mod_count = [0] * 200
    for a_mod in A_mod:
        A_mod_count[a_mod] += 1
    count = 0
    for i in range(200):
        count += A_mod_count[i] * (A_mod_count[i] - 1) // 2
    print(count)
