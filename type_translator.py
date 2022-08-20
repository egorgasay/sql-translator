def print_logic(arrayOfTypes, decision, user_type, translate_to):
    value = None
    for v, k in arrayOfTypes.items():
        keys = k
        if user_type in k:
            value = v
            break
    if not value is None:
        # print("Choose one of this:", end='')
        new_type = translate_to[value]
        answer = []
        for k in range(len(new_type)):
            answer.append(new_type[k])
        return answer[0]
    else:
        if keys[0] == '"char"':
            return 'tinyint'
            # new_type = translate_to['TINYINT'][0]
        else:
            return "UNDEFINED TYPE"


def type_translator(user_type, decision):
    """
    Type translator
    :param user_type: text of user type
    :param decision: PostgreSQL or MSSQL
    :return: correct type or None if it's Keyword
    """
    user_type = user_type
    PostgreSQLArrayOfTypes = {'TINYINT': ('"char"',),
                              'SMALLINT': ('SMALLINT', 'INT2'),
                              'INT': ('INT', 'INTEGER', 'INT4'),
                              'BIGINT': ('BIGINT', 'INT8'),
                              'FLOAT': ('REAL', 'FLOAT(24)'),
                              'DOUBLE': ('DOUBLE PRECISION', 'FLOAT(53)'),
                              'DECIMAL': ('DECIMAL', 'NUMERIC'),
                              'DATE': ('DATE', )}
    MSSQLArrayOfTypes = {'TINYINT': ('tinyint',),
                         'SMALLINT': ('smallint',),
                         'INT': ('int',),
                         'BIGINT': ('bigint',),
                         'FLOAT': ('real', 'float(24)', 'money'),
                         'DOUBLE': ('float', 'float(53)'),
                         'DECIMAL': ('decimal', 'numeric'),
                         'DATE': ('datetime', )}
    if decision == 'PSQL':
        return print_logic(PostgreSQLArrayOfTypes, decision, user_type, MSSQLArrayOfTypes)
    else:
        return print_logic(MSSQLArrayOfTypes, decision, user_type, PostgreSQLArrayOfTypes)

