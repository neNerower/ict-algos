from rank import get_determinant
from transpont import transpont

def get_minor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

# Return inversed matrix
def inverse(m):
    if (len(m) == len(m[0])):
        size = len(m)
    else:
        raise "Matrix must be square"

    determinant = get_determinant(m)

    if (determinant == 0):
        raise "Determinant is zero"

    # Create addition matrix
    addition = []
    for i in range(size):
        addition.append([])
        for j in range(size):
            el = get_determinant(get_minor(m, i, j))
            addition[i].append((-1)**(i+1 + j+1) * el)

    return [[e / determinant for e in row] for row in transpont(addition)]
    

if __name__ == "__main__":
    m = [
        [ 2,  5,  7],
        [ 6,  3,  4],
        [ 5, -2, -3]
    ]

    print("Inversed matrix m:")
    for lst in inverse(m):
        print(lst)
