from flask import Flask, render_template, request, redirect
from database import get_db_connection

app = Flask(__name__)


@app.route("/")
def home():

    conn = get_db_connection()

    posts = conn.execute(
        "SELECT * FROM posts ORDER BY created_at DESC"
    ).fetchall()

    conn.close()

    return render_template("home.html", posts=posts)


@app.route("/post/<int:post_id>")
def post(post_id):

    conn = get_db_connection()

    post = conn.execute(
        "SELECT * FROM posts WHERE id = ?",
        (post_id,)
    ).fetchone()

    comments = conn.execute(
        "SELECT * FROM comments WHERE post_id = ? ORDER BY created_at DESC",
        (post_id,)
    ).fetchall()

    conn.close()

    return render_template(
        "post.html",
        post=post,
        comments=comments
    )


@app.route("/post/<int:post_id>/comment", methods=["POST"])
def add_comment(post_id):

    author = request.form["author"]
    content = request.form["content"]

    if author and content:

        conn = get_db_connection()

        conn.execute(
            "INSERT INTO comments (post_id, author, content) VALUES (?, ?, ?)",
            (post_id, author, content)
        )

        conn.commit()
        conn.close()

    return redirect(f"/post/{post_id}")


@app.route("/create", methods=["GET", "POST"])
def create_post():

    if request.method == "POST":

        title = request.form["title"]
        body = request.form["body"]

        conn = get_db_connection()

        conn.execute(
            "INSERT INTO posts (title, body) VALUES (?, ?)",
            (title, body)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("create_post.html")


@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):

    conn = get_db_connection()

    post = conn.execute(
        "SELECT * FROM posts WHERE id = ?",
        (post_id,)
    ).fetchone()

    if request.method == "POST":

        title = request.form["title"]
        body = request.form["body"]

        conn.execute(
            "UPDATE posts SET title = ?, body = ? WHERE id = ?",
            (title, body, post_id)
        )

        conn.commit()
        conn.close()

        return redirect(f"/post/{post_id}")

    conn.close()

    return render_template("edit_post.html", post=post)


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete_post(post_id):

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM comments WHERE post_id = ?",
        (post_id,)
    )

    conn.execute(
        "DELETE FROM posts WHERE id = ?",
        (post_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)