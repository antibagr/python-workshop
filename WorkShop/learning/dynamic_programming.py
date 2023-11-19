def solve():
    n = 12
    arr = [
        [3, 5, 3, 0, 0, 5, 0, 9, 7, 6, 5, 1],
        [9, 0, 8, 5, 7, 9, 4, 6, 2, 4, 2, 2],
        [8, 0, 5, 9, 9, 3, 8, 5, 3, 7, 4, 4],
        [9, 5, 3, 7, 4, 3, 9, 9, 5, 5, 9, 6],
        [3, 2, 6, 0, 5, 9, 0, 9, 3, 3, 0, 1],
        [7, 0, 1, 7, 9, 0, 1, 4, 7, 1, 4, 4],
        [4, 9, 1, 2, 9, 0, 4, 1, 6, 9, 9, 8],
        [9, 4, 3, 2, 2, 5, 9, 0, 2, 5, 1, 7],
        [0, 4, 4, 1, 9, 7, 1, 5, 3, 6, 9, 2],
        [5, 4, 0, 0, 0, 4, 8, 1, 6, 6, 8, 3],
        [5, 6, 0, 4, 7, 6, 9, 3, 9, 2, 9, 9],
        [5, 0, 3, 2, 9, 6, 1, 5, 1, 8, 1, 1],
    ]
    cache = [[0 for _ in range(n)] for _ in range(n)]
    cache[0][0] = arr[0][0]
    print(cache[0][0], end=" ")
    for i in range(1, n):
        cache[i][0] = cache[i - 1][0] + arr[i][0]
        cache[0][i] = cache[0][i - 1] + arr[0][i]
        print(cache[0][i], end=" ")
    print()
    for i in range(1, n):
        print(cache[i][0], end=" ")
        for j in range(1, n):
            cache[i][j] = (
                arr[i][j] + cache[i - 1][j] + cache[i][j - 1] - cache[i - 1][j - 1]
            )
            print(cache[i][j], end=" ")
        print()
    x1, y1, x2, y2 = map(int, input().split())
    print(cache[x2][y2] - cache[x1 - 1][y2] - cache[x2][y1 - 1] + cache[x1 - 1][y1 - 1])


t = int(input())
for _ in range(t):
    solve()
