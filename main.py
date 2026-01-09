rows, cols = len(grid), len(grid[0])
count = 0
visited = set()

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '1' and (r, c) not in visited:
            count += 1
            stack = [(r, c)]
            visited.add((r, c))

            while stack:
                curr_r, curr_c = stack.pop()

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '1' and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            stack.apped((nr, nc))
return count