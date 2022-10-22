from flask import Flask, request, jsonify
import pickle
import sklearn
model = pickle.load(open('pipe.pkl', 'rb'))
print(model)
column_order = ['critic_likes', 'critic_comments', 'movie_release_year', 'movie_popularity', 'avg_list_comments']
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    data = request.json
    X = [data[col] for col in column_order]
    prediction =model.predict([X])[0]
    return jsonify({"prerdiction": prediction})

app.run()
