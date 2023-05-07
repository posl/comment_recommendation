def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    ans = 0
    for i in range(N_len):
        if i % 3 == 0 and i != 0:
            ans += 1
    print(ans)
