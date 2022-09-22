def transpont(m):
    row_amount = len(m)
    col_amount = len(m[0])

    tm = [[0 for i in range(row_amount)] for j in range(col_amount)]

    for i in range(row_amount):
        for j in range(col_amount):
            tm[j][i] = m[i][j]

    return tm


if __name__ == "main":
    m = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0,0,0]
    ]

    for lst in transpont(m):
        print(lst)
