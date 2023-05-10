def main():
    # T = int(input())
    T = 1
    for i in range(T):
        # a, s = map(int, input().split())
        a, s = 1, 8
        print("Yes" if s >= a and (s - a) % 2 == 0 else "No")
