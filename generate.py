def generate_ones(filename, num_rows, target):
    rows = [f'Target: {target}\n']
    for i in range(num_rows - 1):
        rows.append(('1,' * i) + '1\n')
    rows.append(('1,' * (num_rows // 2 - (1 - (num_rows % 2))) + target + ',' + ('1,' * (num_rows // 2 - 1)) + '1\n'))

    out_file = open(filename, 'w')
    out_file.writelines(rows)
    out_file.close()

if __name__ == '__main__':
    generate_ones(input('filename:\n'), int(input('num rows:\n')), input('target:\n'))