
def solve(matrix: list[list[int]], mod: int):
    for i in range(len(matrix) - 1):
        m = i
        while matrix[m][i] == 0:
            m = m + 1
        alt_row: list[int] = [((num * pow(matrix[m][i], -1, mod)) % mod) for num in matrix[m]]
        for j in range(m + 1, len(matrix)):
            sub_row = [((num * matrix[j][i]) % mod) for num in alt_row]
            matrix[j] = [((matrix[j][k] - sub_row[k]) % mod) for k in range(len(matrix[j]))]

    for i in reversed(range(0, len(matrix))):
        m = i
        while matrix[m][i] == 0:
            m = m - 1
        matrix[i] = [(num * pow(matrix[m][i], -1, mod) % mod) for num in matrix[m]]
        for j in range(m):
            matrix[j] = [((matrix[j][k] - matrix[m][k]*matrix[j][i]) % mod) for k in range(len(matrix[j]))]

    return [matrix[k][len(matrix)] for k in range(len(matrix))]

print(solve([[2,6,1,3030],[11,2,0,6892],[4,1,3,8773]], 9539))