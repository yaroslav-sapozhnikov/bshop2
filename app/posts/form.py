from wtforms import Form, StringField, TextAreaField


class PostForm(Form):
    title = StringField("Ваше имя")
    body = TextAreaField("Отзыв")
