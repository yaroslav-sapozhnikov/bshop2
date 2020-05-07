from wtforms import Form, TextAreaField, RadioField


class PostForm(Form):
    body = TextAreaField("Отзыв")
