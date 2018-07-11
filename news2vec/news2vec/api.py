from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from flask import current_app as app
import json
from werkzeug.exceptions import abort


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/')
def index():
    return json.dumps(app.models.keys())


@bp.route('/<corpus>/most_similar', methods=['GET', 'POST'])
def most_similar(corpus):
    words = request.args.getlist('words')
    years = request.args.getlist('years')
    n = request.args.get('n', default=5, type=int)

    res = app.models[corpus].get_most_similar(words, n, years)

    return json.dumps(res, ensure_ascii=False)


@bp.route('/<corpus>/compare', methods=['GET', 'POST'])
def compare(corpus):
    word1 = request.args.get('word1')
    word2 = request.args.get('word2')
    years = request.args.getlist('years')

    res = app.models[corpus].compare(word1, word2, years)

    # Convert distance values away from float32 to float:
    for key in res:
        res[key] = float(res[key])

    return json.dumps(res, ensure_ascii=False)


@bp.route('/<corpus>/vector_mathematics', methods=['GET', 'POST'])
def vector_mathematics(corpus):
    positive_terms = request.args.getlist('positive_terms')
    negative_terms = request.args.getlist('negative_terms')
    years = request.args.getlist('years')
    n = request.args.get('n', default=5, type=int)

    res = app.models[corpus].word_vector_math(positive_terms,
                                              negative_terms,
                                              n, years)

    return json.dumps(res, ensure_ascii=False)
