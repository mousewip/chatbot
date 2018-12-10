from pyvi.ViPosTagger import ViPosTagger
from pyvi.ViTokenizer import ViTokenizer
from sklearn.base import TransformerMixin, BaseEstimator


class FeatureTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.tokenizer = ViTokenizer()
        self.pos_tagger = ViPosTagger()

    def fit(self, *_):
        return self

    def transform(self, X, y=None, **fit_params):
        result = X.apply(lambda text: self.tokenizer.tokenize(text))
        return result
