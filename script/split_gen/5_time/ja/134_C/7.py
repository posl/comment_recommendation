def main():
    n = int(input())
    a_list = []
    for _ in range(n):
        a = int(input())
        a_list.append(a)
    for i in range(n):
        b_list = a_list.copy()
        b_list.pop(i)
        print(max(b_list))
