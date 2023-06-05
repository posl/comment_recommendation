def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.reverse()
    max_height = 0
    for a in a_list:
        if a >= max_height:
            max_height = a
        else:
            max_height = a + max_height % a
    print(max_height)
