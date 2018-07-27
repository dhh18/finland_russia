class W2VModel:
    def __init__(self, models):
        self.models = models

    def get_most_similar(self, words, n, years=None):
        results = {}
        if not years:
            years = self.models.keys()
        for year in years:
            results[year] = self.models[year].most_similar(positive=words,
                                                           topn=n)

        return results

    def compare(self, word1, word2, years=None):
        results = {}
        if not years:
            years = self.models.keys()
        for year in years:
            try:
                results[year] = self.models[year].similarity(word1, word2)
            except KeyError:
                results[year] = 'N/A'
        return results

    def word_vector_math(self, positive_terms, negative_terms, n, years=None):
        results = {}
        if not years:
            years = self.models.keys()
        for year in years:
            try:
                results[year] = self.models[year].most_similar(positive=positive_terms,
                                                               negative=negative_terms,
                                                               topn=n)
            except KeyError:
                results[year] = [["N/A", "N/A"]]

        return results

    def years(self):
        return self.models.keys()
