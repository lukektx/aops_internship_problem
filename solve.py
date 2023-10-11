import sys

def solve(pyramid, target, side = 'L', row = 0, pos = 0, product = 1):
    product *= pyramid[row][pos]
    if target % pyramid[row][pos] != 0:
        return ''
    elif row == len(pyramid) - 1:
        return side if product == target else ''
    else:
        l_value = solve(pyramid, target, 'L', row + 1, pos, product)
        r_value = solve(pyramid, target, 'R', row + 1, pos + 1, product)
        ret = l_value + r_value
        ret += side if ret else ''
        return ret



if __name__ == '__main__':
    file_name = 'input.txt'
    print(sys.argv)
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    in_file = open(file_name, 'r')
    lines = in_file.readlines()
    in_file.close()
    target_line = lines.pop(0)
    target_num = int(target_line[target_line.index(' '):])
    pyramid = [[int(val) for val in row.rstrip('\n').split(',')] for row in lines]
    print(target_num)
    print(pyramid)
    out_file = open('output.txt', 'w')
    out_val = solve(pyramid, target_num)[1:]
    print(out_val)
    out_file.write(out_val)