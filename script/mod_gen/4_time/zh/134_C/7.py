def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a_max = max(a)
    a.remove(a_max)
    for i in range(n):
        print(a_max)
main()
