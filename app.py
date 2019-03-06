from flask import Flask, request, jsonify
import pickle
from summa import keywords
import utility 

app = Flask(__name__)
# stoppath = "data/stoplists/vi.txt"


@app.route('/',methods=['GET'])
def index():
    return 'OK!'

@app.route('/api/execute',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    text = data['text']
    lang = data['lang']
    ratio = float(data['ratio'])
    stoppath = "data/stoplists/{0}.txt".format(lang)
    
    result = keywords.keywords(text=text, ratio=ratio,additional_stopwords=utility.load_stop_words(stoppath))

    return jsonify(result)
if __name__ == '__main__':
    app.run(port=5000, debug=True)

# print(keywords.keywords(text, 0.2,additional_stopwords=utility.load_stop_words(stoppath)))


