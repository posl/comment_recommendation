def main():
    s = input()
    q = int(input())
    # 0: ABC, 1: BCA, 2: CAB
    t = [0, 1, 2]
    for _ in range(q):
        ti, ki = map(int, input().split())
        ti = ti % 3
        ki -= 1
        if t[ti] == 0:
            print(s[ki])
        elif t[ti] == 1:
            print('B' if s[ki] == 'A' else 'C' if s[ki] == 'B' else 'A')
        else:
            print('C' if s[ki] == 'A' else 'A' if s[ki] == 'B' else 'B')
