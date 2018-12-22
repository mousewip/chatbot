#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.externals import joblib
import os
from sklearn import metrics
from src.model.naive_bayes_model import NaiveBayesModel
from src.model.svm_model import SVMModel

APP_ROOT = os.path.dirname(__file__)


class TextClassificationPredict(object):
    def __init__(self):
        self.test = None
        self.model = joblib.load(APP_ROOT + '/model.sav')
        self.model_conv = joblib.load((APP_ROOT + '/model_conv.sav'))
        print('Load all model success')

    def get_model(self):
        return self.model

    def predict(self, pred_text):
        test_data = []
        test_data.append({"feature": pred_text, "target": ""})
        df_test = pd.DataFrame(test_data)
        predicted = self.model.predict(df_test["feature"])

        # Print predicted result
        print(predicted)
        result = predicted[0]
        proba = self.model.predict_proba(df_test["feature"])
        accu = max(proba[0])
        return result, accu * 100

    def predict_conv(self, pred_text):
        test_data = []
        test_data.append({"feature": pred_text, "target": ""})
        df_test = pd.DataFrame(test_data)
        predicted = self.model_conv.predict(df_test["feature"])

        # Print predicted result
        print(predicted)
        result = predicted[0]
        proba = self.model_conv.predict_proba(df_test["feature"])
        accu = max(proba[0])
        return result, accu * 100

    def train_model_conv(self):
        #  train data
        train_data = []
        train_data.append({"feature": "xin chào", "target": "chao_hoi"})
        train_data.append({"feature": "chào ad", "target": "chao_hoi"})
        train_data.append({"feature": "chào adddd", "target": "chao_hoi"})
        train_data.append({"feature": "chào admin", "target": "chao_hoi"})
        train_data.append({"feature": "xin chào page", "target": "chao_hoi"})
        train_data.append({"feature": "hello", "target": "chao_hoi"})
        train_data.append({"feature": "hellooooooooo", "target": "chao_hoi"})
        train_data.append({"feature": "hi", "target": "chao_hoi"})
        train_data.append({"feature": "chào bạn", "target": "chao_hoi"})
        train_data.append({"feature": "xin chào bạn", "target": "chao_hoi"})
        train_data.append({"feature": "chào bot", "target": "chao_hoi"})
        train_data.append({"feature": "hello bot", "target": "chao_hoi"})
        train_data.append({"feature": "chào buổi sáng", "target": "chao_hoi"})
        train_data.append({"feature": "chào buổi tối", "target": "chao_hoi"})

        train_data.append({"feature": "bot ơi", "target": "tro_giup"})
        train_data.append({"feature": "ad ơi", "target": "tro_giup"})
        train_data.append({"feature": "page ơi", "target": "tro_giup"})
        train_data.append({"feature": "bác sĩ ơi", "target": "tro_giup"})
        train_data.append({"feature": "bác sỹ ơi", "target": "tro_giup"})
        train_data.append({"feature": "weeeee", "target": "tro_giup"})
        train_data.append({"feature": "we", "target": "tro_giup"})
        train_data.append({"feature": "trợ giúp", "target": "tro_giup"})
        train_data.append({"feature": "help", "target": "tro_giup"})
        train_data.append({"feature": "tôi cần hỗ trợ", "target": "tro_giup"})
        train_data.append({"feature": "hỗ trợ", "target": "tro_giup"})
        train_data.append({"feature": "giúp em với", "target": "tro_giup"})
        train_data.append({"feature": "em cần hỗ trợ", "target": "tro_giup"})
        train_data.append({"feature": "gợi ý", "target": "tro_giup"})
        train_data.append({"feature": "cho em hỏi cái này", "target": "tro_giup"})
        train_data.append({"feature": "em có chút vấn đề", "target": "tro_giup"})
        train_data.append({"feature": "tôi có chút vấn đề", "target": "tro_giup"})
        train_data.append({"feature": "em muốn hỏi", "target": "tro_giup"})

        train_data.append({"feature": "bye", "target": "ket_thuc"})
        train_data.append({"feature": "goodbye", "target": "ket_thuc"})
        train_data.append({"feature": "tạm biêt", "target": "ket_thuc"})
        train_data.append({"feature": "cám ơn ad", "target": "ket_thuc"})
        train_data.append({"feature": "cám ơn bot", "target": "ket_thuc"})
        train_data.append({"feature": "cám ơn page", "target": "ket_thuc"})
        train_data.append({"feature": "tks", "target": "ket_thuc"})
        train_data.append({"feature": "thank you", "target": "ket_thuc"})
        train_data.append({"feature": "dạ vâng, em cám ơn ạ", "target": "ket_thuc"})
        train_data.append({"feature": "bái bai", "target": "ket_thuc"})

        train_data.append({"feature": "em cảm thấy đau răng", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "em cảm thấy mệt mỏi", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "em cảm thấy đau răng", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "tôi cảm thấy chóng mặt, buồn nôn, đau bụng", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "dạo này cơ thể cảm thấy mệt mỏi", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "da em bị nổi mụn", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "bé khóc khá nhiều", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "mắt mờ, tầm nhìn thấp, phải nheo mắt khi nhìn", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "tôi hay bị tiểu đêm", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "tôi hay bị đau lưng", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "tôi hay bị nhức mỏi", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "em bị đau bụng", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "em bị trễ kinh", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "em bị ù tai, hoă mắt, chóng mặt", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "đau lưng, mỏi vai", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "ăn không tiêu, khó ngủ, ngủ ngáy", "target": "mo_ta_trieu_chung"})
        train_data.append({"feature": "hay quên, làm trước quên sau", "target": "mo_ta_trieu_chung"})

        df_train = pd.DataFrame(train_data)

        test_data = []
        test_data.append({"feature": "xin chào", "target": "chao_hoi"})
        df_test = pd.DataFrame(test_data)

        # init model naive bayes
        model = NaiveBayesModel()

        clf = model.clf.fit(df_train["feature"], df_train.target)

        joblib.dump(clf, 'model_conv.sav')


        predicted = clf.predict(df_test["feature"])

        # Print predicted result
        print(predicted)
        print(clf.predict_proba(df_test["feature"]))

    def train_model(self):
        #  train data
        df_train = pd.read_json('sk.json')

        test_data = []
        test_data.append({"feature": "tôi bị đau bụng", "target": "đau ruột thừa"})
        df_test = pd.DataFrame(test_data)

        # init model naive bayes
        model = NaiveBayesModel()

        clf = model.clf.fit(df_train["feature"], df_train.target)

        joblib.dump(clf, 'model.sav')


        predicted = clf.predict(df_test["feature"])

        # Print predicted result
        print(predicted)
        print(clf.predict_proba(df_test["feature"]))


if __name__ == '__main__':
    tcp = TextClassificationPredict()

    if not os.path.isfile("model.sav"):
        tcp.train_model()
        print("Train model success")
    else:
        model = joblib.load('model.sav')
        #  test data
        test_data = []
        test_data.append({"feature": "hoa mắt", "target": "cận thị"})
        df_test = pd.DataFrame(test_data)
        predicted = model.predict(df_test["feature"])

        # Print predicted result
        print(predicted)

        ls = model.predict_proba(df_test["feature"])
        # print(ls[0])
        print("accuracy:  %0.3f" % max(ls[0]))

        score = metrics.accuracy_score(df_test.target, predicted)
        print("accuracy:   %0.3f" % score)
