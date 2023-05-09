def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = ['ABC', 'ARC', 'AGC', 'AHC']
    S4.remove(S1)
    S4.remove(S2)
    S4.remove(S3)
    print(S4[0])

if __name__ == '__main__':
    main()