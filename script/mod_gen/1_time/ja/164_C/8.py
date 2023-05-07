def count_unique_elements(list):
    return len(set(list))
n = int(input())
s = [input() for i in range(n)]
print(count_unique_elements(s))

if __name__ == '__main__':
    count_unique_elements()