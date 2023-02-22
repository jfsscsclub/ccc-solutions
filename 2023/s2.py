# CCC '23 S2 - Roy Zhang
N = int(input())
hills = [int(i) for i in input().split(" ")]

# initialize grid
grid = []
for i in range(N):
    grid.append([0] * N)

# solve
ans = [float('infinity')] * N
ans[0] = 0
for j in range(1, N):
    for i in range(j - 1, -1, -1):
        grid[i][j] = grid[i + 1][j - 1] + abs(hills[i] - hills[j])
        if grid[i][j] < ans[j - i]:
            ans[j - i] = grid[i][j]

print(" ".join(str(i) for i in ans))