from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index_tailwind.html')


if __name__ == '__main__':
    app.run(debug=True)



#https://github.com/hantswilliams/HHA_504_2023/blob/main/WK5/assignment5.md