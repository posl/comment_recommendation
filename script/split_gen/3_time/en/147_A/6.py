def main():
    A = input().split()
    A = [int(i) for i in A]
    if sum(A) >= 22:
        print('bust')
    else:
        print('win')
