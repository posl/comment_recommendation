def main():
    N = int(input())
    mod = 10**9+7
    print(2*(10**N-9**N-9**N+8**N)%mod)
