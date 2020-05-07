from flask import Blueprint
from flask import render_template
from models import Post
from .form import PostForm
from app import db
from flask import request
from flask import redirect
from flask import url_for
from flask_security import login_required
from flask_security import current_user


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():
    if request.method == 'POST':
        rate = request.form["inlineRadioOptions"]
        body = request.form['body']
        try:
            post = Post(username=current_user.username, body=body, rate=rate)
            db.session.add(post)
            db.session.commit()
        except:
            print('something went wrong')
        
        return redirect(url_for('posts.index'))
    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():
    posts = Post.query.order_by(Post.id.desc())
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    pages = posts.paginate(page=page, per_page=5)

    return render_template('posts/index.html', posts=posts, pages=pages)
