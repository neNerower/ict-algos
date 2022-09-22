def transpont(m):
    row_amount = len(m)
    col_amount = len(m[0])

    tm = [[0 for i in range(row_amount)] for j in range(col_amount)]

    for i in range(row_amount):
        for j in range(col_amount):
            tm[j][i] = m[i][j]

    return tm


def mult(a,b):
    if (len(a[0]) == len(b)):
        common_side = len(b)
    else:
        raise "Impossible to multiply matrixes"

    res_rows = len(a)
    res_cols = len(b[0])

    res = []

    for i in range(res_rows):
        res.append([])

        for j in range(res_cols):
            sum = 0

            for r in range(common_side):
                sum += a[i][r] * b[r][j]

            res[i].append(sum)

    return res



if __name__ == "__main__":
    m = [
        [ 6, 3, -1, 0],
        [ 1, 1,  0, 4],
        [-2, 5,  0, 2]
    ]

    n = [
        [2, 1, 4],
        [0, 1, 1]
    ]

    # from pprint import pprint as pp

    print("Transpont matrix m:")
    # pp(transpont(m))
    for lst in transpont(m):
        print(lst)

    print("\n\nMultiply matrix n with m:")
    # pp(mult(n,m))
    for lst in mult(n,m):
        print(lst)