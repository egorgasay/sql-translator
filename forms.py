from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, HiddenField, TextAreaField


class CommonForm(FlaskForm):
    list_db = [('PSQL', 'PostgreSQL'), ('MSSQL', 'Microsoft SQL Server')]

    source_db = SelectField(
        'Выберите исходный диалект',
        coerce=str,
        choices=list_db,
        render_kw={
            'class': 'form-control',
            'style': 'height: 80px; font-size: 28px'
        }
    )
    final_db = SelectField(
        'Выберите диалект на который нужно перевести',
        coerce=str,
        choices=list_db[::-1],
        render_kw={
            'class': 'form-control',
            'style': 'height: 80px; font-size: 28px; '
        }
    )

    text = TextAreaField(label='Текст запроса',
                         render_kw={
                             'class': 'form-control',
                             'style': 'height: 180px; width: 200%; ',
                         }
                         )
    submit = SubmitField("Перевести",
                         render_kw={
                             'class': 'form-control',
                             'style': 'height: 80px; width: 30%; font-size: 28px'
                         }
                         )
    # position = TextAreaField("HiddenField")
    # pre_pos = TextAreaField("HiddenField")