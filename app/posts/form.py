from wtforms import Form, TextAreaField


class PostForm(Form):
    body = TextAreaField("Отзыв")
