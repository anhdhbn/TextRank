from summa import keywords
import utility 

print("---------------- ahihi")
stoppath = "data/stoplists/vi.txt"

sample_file = open("data/docs/vi/test.txt", 'r')
text = sample_file.read()


print(keywords.keywords(text, 0.3,additional_stopwords=utility.load_stop_words(stoppath)))


