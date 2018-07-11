from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
import json
from werkzeug.exceptions import abort
from flask import current_app as app

bp = Blueprint('view', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/most_similar', methods=['GET'])
def most_similar():
    results = None
    words = request.args.get('words')
    corpora = request.args.getlist('corpora')
    if words and corpora:
        words = [word.strip() for word in words.split(',')]
        n = request.args.get('n', type=int)
        results = {}
        for corpus in corpora:
            results[corpus] = app.models[corpus].get_most_similar(words, n)
    return render_template('most_similar.html',
                            models=app.models,
                            results=results,
                            args=request.args)


@bp.route('/compare')
def compare():
    results = None
    word1 = request.args.get('word1')
    word2 = request.args.get('word2')
    corpora = request.args.getlist('corpora')
    if word1 and word2 and corpora:
        results = {}
        for corpus in corpora:
            results[corpus] = app.models[corpus].compare(word1, word2)
    return render_template('compare.html',
                            models=app.models,
                            results=results,
                            args=request.args)


@bp.route('/vector_mathematics')
def vector_mathematics():
    results = None
    positive_words = request.args.get('positive_words')
    negative_words = request.args.get('negative_words')
    corpora = request.args.getlist('corpora')
    if positive_words and negative_words and corpora:
        positive_words = [word.strip() for word in positive_words.split(',')]
        negative_words = [word.strip() for word in negative_words.split(',')]
        n = request.args.get('n', type=int)
        results = {}
        for corpus in corpora:
            results[corpus] = app.models[corpus].word_vector_math(positive_words,
                                                                  negative_words, n)
    return render_template('vector_mathematics.html',
                            models=app.models,
                            results=results,
                            args=request.args)