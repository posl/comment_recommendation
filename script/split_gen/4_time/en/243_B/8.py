def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_set = set(a)
    b_set = set(b)
    same = 0
    diff = 0
    for i in range(n):
        if a[i] == b[i]:
            same += 1
        elif a[i] in b_set:
            diff += 1
    print(same)
    print(diff)
