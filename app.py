from flask import Flask, render_template


#app = Flask(__name__)

app = Flask(__name__,static_folder="/templates")


@app.route('/')
def index():
    return render_template('index_tailwind.html')


if __name__ == '__main__':
    app.run(debug=True)



