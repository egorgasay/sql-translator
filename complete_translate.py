from type_translator import type_translator


def translator(query, decision):
    query = query.split(' ')
    types_psql = ('"char"', 'SMALLINT', 'INT2', 'INT', 'INTEGER', 'INT4', 'BIGINT', 'INT8',
                  'REAL', 'FLOAT(24)', 'money', 'DOUBLE PRECISION', 'FLOAT(53)', 'DECIMAL',
                  'NUMERIC', 'DATE')
    types_mssql = ('tinyint', 'smallint', 'int', 'bigint', 'real', 'float(24)', 'float',
                  'float(53)', 'decimal', 'numeric', 'datetime')

    for i in range(len(query)):
        if query[i] in types_psql or query[i] in types_mssql and not query[i+1] == 'IDENTITY':
            # query[i] = ' '.join(type_translator(query[i], decision))
            query[i] = type_translator(query[i], decision)
    # print(query)
    return ' '.join(query)
