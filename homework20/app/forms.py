from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired

class OptionForm(FlaskForm):
    text = StringField("Вариант", validators=[DataRequired()])

class PollForm(FlaskForm):
    question = StringField("Вопрос", validators=[DataRequired()])
    options = FieldList(FormField(OptionForm), min_entries=2, max_entries=5)
    submit = SubmitField("Создать опрос")
