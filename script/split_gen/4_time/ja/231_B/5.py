def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(max(set(s),key=s.count))
main()
