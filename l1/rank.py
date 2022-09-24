def get_sub_matrix(matrix, rows, cols):
    """
    This function returns the copy of the matrix containing target rows and columns
    @params:
        matrix - matrix to copy from
        rows - list of rows to copy
        cols - list of columns to copy
    """
    res = []

    for i in range(len(matrix)):
        if i not in rows:
            continue
        
        lst = []

        for j in range(len(matrix[i])):
            if j not in cols:
                continue

            lst.append(matrix[i][j])
        
        res.append(lst)

    return res


def get_determinant(m) -> int:
    """
    Count determinant of the matrix
    @params:
        m - matrix to count determinant from
    """
    if len(m) == len(m[0]):
        # TODO: Check that size is not less than 2
        size = len(m)
    else:
        raise "Matrix must be square"

    # Just a stub for now
    # TODO: Remove from here
    if size == 1:
        return m[0][0]

    if size == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    res = 0
    for col in range(size):
        res += (-1 if col%2 !=0 else 1) * m[0][col] * get_determinant(get_sub_matrix(m, [i for i in range(size) if i != 0], [i for i in range(size) if i != col]))
    
    return res
    

def get_matrix_rank(m):
    """
    This function returns the rank of the matrix
    The minor method is used
    @params:
        m - matrix to get the rank from
    """
    rows_amount = len(m)
    cols_amount = len(m[0])

    minor_rows = []
    minor_cols = []

    is_ranked = True

    while is_ranked:
        is_ranked = False

        for i in range(rows_amount):
            if i in minor_rows:
                continue

            for j in range(cols_amount):
                if j in minor_cols:
                    continue

                if get_determinant(get_sub_matrix(m, [*minor_rows, i], [*minor_cols, j])) != 0:
                    minor_rows.append(i)
                    minor_cols.append(j)
                    is_ranked = True

                if is_ranked:
                    break
            
            if is_ranked:
                    break

    return len(minor_rows)


if __name__ == "__main__":
    m = [
        [ 1,  2,  0, 5],
        [ 2,  4, -1, 0],
        [-2, -4,  1, 0],
        [ 1,  0,  2, 1]
    ]

    n = [[0 for i in range(3)] for j in range(3)]

    print(get_matrix_rank(m))
