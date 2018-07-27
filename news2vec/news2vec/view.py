from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
import json
from werkzeug.exceptions import abort
from flask import current_app as app
from werkzeug.datastructures import MultiDict
from . import auth

bp = Blueprint('view', __name__)


def get_download_path(corpus, param_string, filetype='xls'):
    pass


def validate_input(param):
    if len(param) > 30:
        return False
    return True


@bp.route('/')
@auth.requires_auth
def index():
    return render_template('index.html')


@bp.route('/most_similar', methods=['GET'])
@auth.requires_auth
def most_similar():
    results = None
    download_paths = {}
    words = request.args.get('words')
    corpora = request.args.getlist('corpora')
    if words and corpora:
        words = [word.strip() for word in words.split(',')]
        n = request.args.get('n', type=int)
        for param in words + corpora:
            if not validate_input(param):
                flash("Input is too long")
                return redirect(url_for('view.most_similar'))
        results = {}

        multiparams = MultiDict({'words': words, 'n': n})
        for corpus in corpora:
            try:
                results[corpus] = app.models[corpus].get_most_similar(words, n)
            except KeyError as e:
                flash("{} in {}".format(str(e).strip('\"'), corpus))

            download_paths[corpus] = get_download_path(corpus,
                                                       multiparams,
                                                       filetype='xls')
    return render_template('most_similar.html',
                            models=app.models,
                            results=results,
                            args=request.args)


@bp.route('/compare')
@auth.requires_auth
def compare():
    results = None
    word1 = request.args.get('word1')
    word2 = request.args.get('word2')
    corpora = request.args.getlist('corpora')
    if word1 and word2 and corpora:
        results = {}
        for param in [word1] + [word2] + corpora:
            if not validate_input(param):
                flash("Input is too long")
                return redirect(url_for('view.compare'))
        for corpus in corpora:
            results[corpus] = app.models[corpus].compare(word1, word2)
    return render_template('compare.html',
                            models=app.models,
                            results=results,
                            args=request.args)


@bp.route('/vector_mathematics')
@auth.requires_auth
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
        for param in positive_words + negative_words + corpora:
            if not validate_input(param):
                flash("Input is too long")
                return redirect(url_for('view.vector_mathematics'))
        for corpus in corpora:
            results[corpus] = app.models[corpus].word_vector_math(positive_words,
                                                                  negative_words, n)
    return render_template('vector_mathematics.html',
                            models=app.models,
                            results=results,
                            args=request.args)