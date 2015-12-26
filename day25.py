#Enter the code at row 2947, column 3029.

row = 2947
col = 3029

# row = 6
# col = 6

diagonal_limit = row + col

codes = [[None] * diagonal_limit for y in range(diagonal_limit)]
counter = 20151125
diagonal_length = 1
while diagonal_length < diagonal_limit:
    print diagonal_length
    for i in range(diagonal_length):
        codes[diagonal_length-1-i][i] = counter
        counter *= 252533
        counter %= 33554393

    diagonal_length += 1


# for line in codes:
#     print ["%8d" % (d) for d in line if d is not None]

print "Code is: ", codes[row-1][col-1]
