import sys

# recursive function to solve a pyramid


def solve(pyramid, target, side='', row=0, pos=0, product=1):
    # current product *= the position we're examining
    product *= pyramid[row][pos]

    # if target # isn't divisible by product, we're on the wrong path
    if target % product != 0:
        return ''
    elif row == len(pyramid) - 1:
        return side if product == target else ''
    else:
        l_value = solve(pyramid, target, 'L', row + 1, pos, product)
        r_value = solve(pyramid, target, 'R', row + 1, pos + 1, product)
        # add to current return string if correct path found (recursive call not empty string)
        ret = l_value + r_value
        ret = (side if ret else '') + ret
        return ret


if __name__ == '__main__':
    # get input file name from command line arguments, or default to input.txt
    file_name = 'input.txt'
    if len(sys.argv) == 2:
        file_name = sys.argv[1]

    in_file = open(file_name, 'r')
    lines = in_file.readlines()
    in_file.close()

    # get target value
    target_line = lines.pop(0)
    target_num = int(target_line[target_line.index(' '):])

    # parse input pyramid into 2d int array
    pyramid = [[int(val) for val in row.rstrip('\n').split(',')]
               for row in lines]

    # write solution to output.txt and print
    out_file = open('output.txt', 'w')
    out_val = solve(pyramid, target_num)
    print(out_val)
    out_file.write(out_val)
