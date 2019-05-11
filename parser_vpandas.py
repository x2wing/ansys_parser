import pandas as pd


def preprocessor(src):
    with open('tmp', mode='w') as tmp:
        with open(src, mode='r') as src:
            for str_ in src:
                if str_.find('ANSYS') > 0 or str_.find('TIME') > 0 or str_.find('SEQV') > 0:
                    pass
                else:
                    tmp.write(str_)


def make_df(src):
    df = pd.read_csv(src, header=None, delim_whitespace=True)
    pd.options.display.float_format = '{:e}'.format
    print(df)
    df.to_csv('out.csv', header=False, index=False, sep=';', decimal=",")


def postprocessor(src):
    pass


if __name__ == '__main__':
    file = 'ansys3.txt'
    file = 'ansysM035.txt'
    preprocessor('ansys3.txt')
    make_df('tmp')
    # postprocessor()
