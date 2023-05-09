def main():
    n = int(raw_input())
    a = []
    for i in range(n):
        a.append(raw_input())
    print max(set(a), key=a.count)
