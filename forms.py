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
            'style': 'width: auto'
        }
    )
    final_db = SelectField(
        'Выберите диалект на который нужно перевести',
        coerce=str,
        choices=list_db,
        render_kw={
            'class': 'form-control',
            'style': 'width: auto; padding-left: 100'
        }
    )

    text = TextAreaField(label='Текст запроса',
                         render_kw={
                             'class': 'form-control',
                             'style': 'width: 110%;',
                         }
                         )
    submit = SubmitField("Перевести",
                         render_kw={
                             'class': 'form-control',
                             'style': 'width: auto;'
                         }
                         )
    # position = TextAreaField("HiddenField")
    # pre_pos = TextAreaField("HiddenField")