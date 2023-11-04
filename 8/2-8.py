def maximum_num(grid):
    n = len(grid)
    north_view = [0] * n  # 각 열의 최대 높이
    west_view = [0] * n   # 각 행의 최대 높이

    for i in range(n):
        for j in range(n):
            north_view[j] = max(north_view[j], int(grid[i][j]))
            west_view[i] = max(west_view[i], int(grid[i][j]))
    # grid의 모든 좌표 값을 인자로 받으며 각 행과 열에서 가장 높은 높이를 저장함.
    
    count = 0
    for i in range(n):
        for j in range(n):
            max_height = min(north_view[j], west_view[i])
            height = int(grid[i][j])
            # 최대 높이와 현재 높이의 차이만큼을 합산할 때, 각 자리의 최댓값이 9를 초과하지 않도록 함
            count += max_height - height
    #count 변수를 새로 추가하여 추가 가능한 블록의 수를 계산
    #각 칸에 대해 북쪽 시점과 서쪽 시점 중 낮은 값으로 추가 가능한 높이를 결정하고
    #현재 높이를 빼서 그 칸에 추가할 수 있는 블록의 수를 계산한다.
    return count


n = int(input())
grid = [input() for _ in range(n)]
#사용자로부터 n 값을 입력받아 정수로 변환하고,
#n번 만큼 반복하면서 각 줄의 높이 정보를 입력받아 grid 리스트에 저장

print(maximum_num(grid))
