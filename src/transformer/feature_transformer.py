from pyvi.ViPosTagger import ViPosTagger
from pyvi.ViTokenizer import ViTokenizer
from sklearn.base import TransformerMixin, BaseEstimator
from underthesea import word_tokenize
import unicodedata, re

def no_accent_vietnamese_unicode(s):
    s = re.sub('Đ', 'D', s)
    s = re.sub('đ', 'd', s)
    nkfd_form = unicodedata.normalize('NFKD', s)
    return "".join([c for c in nkfd_form if not unicodedata.combining(c)])


class FeatureTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.tokenizer = ViTokenizer()
        self.pos_tagger = ViPosTagger()

    def fit(self, *_):
        return self

    def transform(self, X, y=None, **fit_params):
        result = X.apply(lambda text: self.tokenizer.tokenize(no_accent_vietnamese_unicode(text)))
        # result = X.apply(lambda text: word_tokenize(text, format='text'))
        print(result)
        return result
