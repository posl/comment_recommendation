def main():
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    dx, dy = map(int, input().split())
    ab = (bx - ax, by - ay)
    bc = (cx - bx, cy - by)
    cd = (dx - cx, dy - cy)
    da = (ax - dx, ay - dy)
    ab_bc = ab[0] * bc[1] - ab[1] * bc[0]
    bc_cd = bc[0] * cd[1] - bc[1] * cd[0]
    cd_da = cd[0] * da[1] - cd[1] * da[0]
    da_ab = da[0] * ab[1] - da[1] * ab[0]
    if ab_bc >= 0 and bc_cd >= 0 and cd_da >= 0 and da_ab >= 0:
        print("Yes")
    else:
        print("No")
