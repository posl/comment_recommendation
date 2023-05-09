def main():
    # Input
    M = int(input())
    uv = [list(map(int, input().split())) for _ in range(M)]
    p = list(map(int, input().split()))
    # Solve
    # 0: empty
    # 1-8: piece
    # 9-17: vertex
    # 18-25: edge
    # 26-33: vertex-edge
    # 34-41: edge-edge
    # 42-49: vertex-vertex-edge
    # 50-57: vertex-edge-edge
    # 58-65: edge-edge-edge
    # 66-73: vertex-vertex-vertex-edge
    # 74-81: vertex-vertex-edge-edge
    # 82-89: vertex-edge-edge-edge
    # 90-97: edge-edge-edge-edge
    # 98-105: vertex-vertex-vertex-vertex-edge
    # 106-113: vertex-vertex-vertex-edge-edge
    # 114-121: vertex-vertex-edge-edge-edge
    # 122-129: vertex-edge-edge-edge-edge
    # 130-137: edge-edge-edge-edge-edge
    # 138-145: vertex-vertex-vertex-vertex-vertex-edge
    # 146-153: vertex-vertex-vertex-vertex-edge-edge
    # 154-161: vertex-vertex-vertex-edge-edge-edge
    # 162-169: vertex-vertex-edge-edge-edge-edge
    # 170-177: vertex-edge-edge-edge-edge-edge
    # 178-185: edge-edge-edge-edge-edge-edge
    # 186-193: vertex-vertex-vertex-vertex-vertex-vertex
    # 194-201: vertex-vertex-vertex-vertex-vertex-edge-edge
    # 202-209: vertex-vertex-vertex-vertex-edge-edge-edge
    # 210-217: vertex-vertex-vertex-edge-edge-edge-edge
    # 218-225: vertex-vertex-edge-edge-edge-edge-edge
    # 226-233: vertex-edge-edge-edge-edge-edge-edge
    # 234-241: edge-edge-edge-edge-edge-edge-edge
    # 242-249: vertex-vertex-vertex-vertex-vertex-vertex-edge
    # 250-257: vertex-vertex-vertex

if __name__ == '__main__':
    main()