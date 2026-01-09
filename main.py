import sys

# 입력 속도를 높이기 위한 설정
r = sys.stdin.readline


def num_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    count = 0

    def dfs(start_r, start_c):
        stack = [(start_r, start_c)]
        visited.add((start_r, start_c))  # 시작점 방문 처리

        while stack:
            curr_r, curr_c = stack.pop()

            # 상하좌우 탐색
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = curr_r + dr, curr_c + dc

                # 범위 내에 있고, '1'이며, 방문하지 않았다면
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '1' and (nr, nc) not in visited:
                        visited.add((nr, nc))  # 스택에 넣을 때 방문 처리 (중복 방지)
                        stack.append((nr, nc))

    # 전체 격자를 순회하며 탐색하지 않은 '1'을 찾음
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and (i, j) not in visited:
                dfs(i, j)  # 연결된 모든 땅을 방문 처리
                count += 1  # 섬의 개수 증가

    return count


# --- 메인 실행 로직 ---

# 1. N (지도의 크기) 입력 받기
try:
    input_line = r().strip()
    if not input_line:
        n = 0
    else:
        n = int(input_line)
except ValueError:
    n = 0

# 2. 지도(Grid) 데이터 입력 받기
# 공백 없이 "0110100" 형태로 들어오는 경우 list(문자열)로 쪼개야 함
grid = []
for _ in range(n):
    line = r().strip()  # 줄바꿈 문자 제거
    grid.append(list(line))

# 3. 함수 실행 및 결과 출력
# n이 아니라 만들어진 grid를 넘겨야 합니다.
result = num_islands(grid)
print(result)


# test input
"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
