from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import csv

# match the tf-idf of each word in each sentence
def sentence_with_tf_idf(weight, word_dict, sentence):
    tf_idf = []
    for word in sentence:
        word_index = word_dict.index(word)
        tf_idf.append(weight[word_index])
    return tf_idf

# calculate the sum of tf-idf in the slide window
def tf_idf_slide_window(sentence_tf_idf, slide_size):
    segment_index = []
    max_tf_idf = 0
    for i in range(5):
        tf_idf = sum(sentence_tf_idf[i:i+slide_size])
        if tf_idf > max_tf_idf:
            segment_index = (i, i+slide_size)
            max_tf_idf = tf_idf
    return segment_index


def word_clip(sentences, sentence_tf_idf, length):
    # clip the sentences to suit for the train_length
    train_segment_index = tf_idf_slide_window(sentence_tf_idf, length)
    train_sample = sentences[train_segment_index[0]: train_segment_index[1]]
    return train_sample


def word_extend(sentences, sentence_tf_idf, length):
    # replicate the sentences to suit for the train_length
    sample_len = len(sentences)
    n_replicate = length // sample_len
    remain_extend = length % sample_len
    sample_first_part = sentences * n_replicate
    slide_index = tf_idf_slide_window(sentence_tf_idf, remain_extend)
    sample_second_part = sentence[slide_index[0]: slide_index[1]]
    train_sample = sample_first_part + sample_second_part
    return train_sample
   

if __name__ == '__main__':
    print('Processing...')
    # read data from file
    data = pd.read_csv('trainTemp2.csv')
    corpus = data['word_seg']
    labels = data['class']
    
    # calculate tf-idf of all word
    tfidf=TfidfVectorizer(max_df=1.0, min_df=1)
    
    # tf-idf value in the word-bag
    weight = tfidf.fit_transform(corpus).toarray()
    
    # all word in the word-bag
    word = tfidf.get_feature_names()
    
    # setting the length of training sentence
    train_length = 2000
#    train = np.zeros((5, train_length))
    train_file = 'train_file.csv'
    with open(train_file, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        for i in range(2):
            sentence = corpus[i].split()
            label = labels[i]
            sentence_tf_idf = sentence_with_tf_idf(weight[i, :], word, sentence)
            if len(sentence) > 2000:
                # select the segment with largest tf-idf
                sample = word_clip(sentence, sentence_tf_idf, train_length)
            else:
                # replicate the sentence to suit for the train_length
                sample = word_extend(sentence, sentence_tf_idf, train_length)
#            train[i, :] = np.array(sample)
            sample.append(str(label))
            writer.writerow(sample)
            print(i, 'OK')
    print(r"It's done ! ^_^ ")