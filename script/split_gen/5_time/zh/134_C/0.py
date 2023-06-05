def main():
    n = int(input())
    a_list = []
    for i in range(n):
        a_list.append(int(input()))
    for i in range(n):
        print(max(a_list[:i] + a_list[i+1:]))
