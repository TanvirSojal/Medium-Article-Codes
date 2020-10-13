# author: Sojal
# n-queen board conflict checking in O(n) time
# using O(n) space

def conflict(board):
    n = len(board)

    row_frequency = [0] * n
    main_diag_frequency = [0] * (2 * n)
    secondary_diag_frequency = [0] * (2 * n)

    for i in range(n):
        row_frequency[board[i]] += 1
        main_diag_frequency[board[i] + i] += 1
        secondary_diag_frequency[n - board[i] + i] += 1

    # print(row_frequency)
    # print(main_diag_frequency)
    # print(secondary_diag_frequency)

    conflicts = 0
    # formula: (N * (N - 1)) / 2
    for i in range(2*n):
        if i < n:
            conflicts += (row_frequency[i] * (row_frequency[i]-1)) / 2
        conflicts += (main_diag_frequency[i] * (main_diag_frequency[i]-1)) / 2
        conflicts += (secondary_diag_frequency[i]
                      * (secondary_diag_frequency[i]-1)) / 2
    return int(conflicts)


# test board
# 0 - indexed row / column values
board = [2, 3, 2, 1]
conflicts = conflict(board)
print(conflicts)
