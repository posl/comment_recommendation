def main():
    N=int(input())
    S=input()
    if S=="OR":
        print(2**N)
    else:
        print(2**(N-1))
