def intersect(r1, r2):
    case1 = r1[2] >= r2[2] and r1[3] >= r2[3] and r1[0] <= r2[0]
    case2 = r2[2] >= r1[2] and r2[3] >= r1[3] and r2[0] <= r1[0]
    case3 = 
     


n = int(input())
rects = []
for i in range(n):
    xl, yl, xr, yr = input().split(" ")
    xl = int(xl)
    yl = int(yl)
    xr = int(xr)
    yr = int(yr)
    rects.append([xl,yl,xr,yr])

for i in range(n):
    for j in range(i, n):

