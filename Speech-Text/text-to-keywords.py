from nltk.stem import PorterStemmer

def text2keywords(text):
    ps = PorterStemmer()
    data = []
    for i in text.split():
        temp = ps.stem(i)
        print(temp)
        if len(temp) > 3:
            data.append(temp)
    return data

text = "I am having fever and some cough"
print(text2keywords(text))
