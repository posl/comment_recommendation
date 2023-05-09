def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    H_ave = [abs(T - h * 0.006 - A) for h in H]
    print(H_ave.index(min(H_ave)) + 1)
