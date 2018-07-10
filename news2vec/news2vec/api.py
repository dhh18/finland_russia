from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
import json
from werkzeug.exceptions import abort
from . import data_loader

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/')
def index():
    return ('foo')


@bp.route('/<corpus>/most_similar', methods=['GET', 'POST'])
def most_similar(corpus):
    words = request.args.getlist('words')
    years = request.args.getlist('years')
    n = request.args.get('n', default=5, type=int)

    try:
        res = data_loader.models[corpus].get_most_similar(words, years, n)
    except ValueError:
        print("Something went wrong")

    return json.dumps(res, ensure_ascii=False)


@bp.route('/<corpus>/compare', methods=['GET', 'POST'])
def compare(corpus):
    word1 = request.args.get('word1')
    word2 = request.args.get('word2')
    years = request.args.getlist('years')

    try:
        res = data_loader.models[corpus].compare_words(word1, word2, years)
    except ValueError:
        print("Something went wrong")

    return res


@bp.route('/<corpus>/vector_mathematics', methods=['GET', 'POST'])
def vector_mathematics(corpus):
    positive_terms = request.args.getlist('positive_terms')
    negative_terms = request.args.getlist('negative_terms')
    years = request.args.getlist('years')
    n = request.args.get('n', default=5, type=int)

    try:
        res = data_loader.models[corpus].word_vector_math(positive_terms,
                                                          negative_terms,
                                                          years, n)
    except ValueError:
        print("Something went wrong")

    return res
