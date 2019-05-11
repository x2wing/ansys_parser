import re


def parse(src):
    regex = r"(.*TIME.*|.*SEQV.*|.*ANSYS.*|)"
    whitespace = r"\s+"
    with open(f'{src}.csv', 'w') as tmp:
        with open(src, mode='r') as src:
            for test_str in src:
                result = re.match(regex, test_str)
                str_ = test_str.strip()
                if str_ and result.group(0) == "":
                    str_ = re.sub(whitespace, ';', str_)
                    str_ = str_.replace('.', ',')
                    print(str_)
                    tmp.write(str_)
                    tmp.write('\n')


if __name__ == '__main__':
    parse('ansys3.txt')
