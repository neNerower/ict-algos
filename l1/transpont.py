def transpont(m):
    """
    Transpont a matrix
    """
    row_amount = len(m)
    col_amount = len(m[0])

    tm = [[0 for i in range(row_amount)] for j in range(col_amount)]

    for i in range(row_amount):
        for j in range(col_amount):
            tm[j][i] = m[i][j]

    return tm



if __name__ == "__main__":
    a = [
        [ 6, 3, -1, 0],
        [ 1, 1,  0, 4],
        [-2, 5,  0, 2]
    ]


    print("Transpont matrix a:")
    for lst in transpont(a):
        print(lst)