def mean_arterial_pressure(A, B):
    return ((A-B)/(3)) + B
A, B = map(int, input().split())
print(mean_arterial_pressure(A, B))

if __name__ == '__main__':
    mean_arterial_pressure()