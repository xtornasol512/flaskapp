from flask import Flask, render_template


app = Flask(__name__)
app.debug = True


@app.route("/")
def hello():
    return "Hello World with FLask!"

@app.route("/LetsRock/")
def rock():
    return "Rocking With Routing!!"

@app.route('/hola/')
@app.route('/hola/<nombre>')
def hello_name(nombre='Mundo'):
    return 'Hey hola %s !!' % nombre

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_template(name=None):
    return render_template('hello.html', name=name)




if __name__ == "__main__":
    app.run(host='0.0.0.0')