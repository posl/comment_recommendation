def solve():
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    s = input()
    print(7 - days.index(s))

if __name__ == '__main__':
    solve()