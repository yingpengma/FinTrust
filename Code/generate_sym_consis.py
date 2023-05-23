import numpy as np
import re

def split_into_sub_sentences(input_text):
    # Split the input text into sentences using regular expressions
    sentences = re.split(r'(?<=[,.] )', input_text)
    return sentences

def make_sym():
    test_list = np.load("earnings_call_3days.npy")
    for i in test_list:
        text = i[3].replace('\n','.\n')
        text = text.split('\n')
        sym_text = ''
        for j in text:
            text = split_into_sub_sentences(j.lower())
            text[-1] = text[-1][:-1]+','
            text[-1] += ' '
            for k in range(len(text)):
                if k == len(text)-1:
                    sym_text += text[-k-1][:-2]
                    sym_text += '. '
                else:
                    sym_text += text[-k-1]
        i[3] = sym_text.replace('. ','\n')
    np.save("sym_earnings_call_3days.npy", test_list)


if __name__ == "__main__":
    make_sym()