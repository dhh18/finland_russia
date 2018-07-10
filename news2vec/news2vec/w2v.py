class W2VModel:
    def __init__(self, models):
        self.models = models

    def get_most_similar(self, words, years, n):
        results = {}
        for year in years:
            results[year] = self.models[year].most_similar(positive=words,
                                                           topn=n)

        return results

    def compare_words(self, word1, word2, years):
        results = {}
        for year in years:
            results[year] = self.models[year].similarity(word1, word2)

        return results

    def word_vector_math(self, positive_terms, negative_terms, years, n):
        results = {}
        for year in years:
            results[year] = self.models[year].most_similar(positive=positive_terms,
                                                           negative=negative_terms,
                                                           topn=n)

        return results

    def years(self):
        return self.models.keys()
