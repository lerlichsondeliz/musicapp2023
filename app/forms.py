from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class NewArtistForm(FlaskForm):
    name = StringField('Artist Name', validators=[DataRequired()])
    songs = TextAreaField('Songs')
    general_info = TextAreaField('General Info')
    submit = SubmitField('Add Artist')
