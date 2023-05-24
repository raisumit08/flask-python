from flask import Flask, render_template
from my_functions import calculate_result, main
# from my_functions import img1
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    result = calculate_result()
    return render_template('index.html', result)

@app.route('/my-endpoint', methods=['POST'])
def my_endpoint():
    data = request.get_json()
    myVariable = data['variable']
    # Process the variable on the server-side
    resul = main(myVariable,'https://i.postimg.cc/HLrk9ZND/Photo-on-09-05-23-at-19-51.jpg')
    return jsonify(result=resul)


if __name__ == '__main__':
    app.debug = True
    app.run()
