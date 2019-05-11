import re


def parser(src):
    regex = r'.*TIME|.*ANSYS|.*UY|.*SEQV'
    whitespace = r"\s+"
    with open(f'{src}.csv', 'w') as out:
        for str_ in open(src, mode='r'):
            match = re.search(regex, str_)
            result = str_.strip()
            if not match and result:
                result = re.sub(whitespace, ';', result).replace('.', ',')
                print(type(result), result)
                out.write(result)


if __name__ == '__main__':
    parser('ansys3.txt')
