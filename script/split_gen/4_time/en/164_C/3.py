def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(len(list(set(s))))
