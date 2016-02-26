from nltk.tag import StanfordNERTagger
#from nltk.tag.stanford import NERTagger

st = StanfordNERTagger('/Users/divya/Desktop/neighborly-serenity/english.all.3class.distsim.crf.ser.gz','/Users/divya/Desktop/neighborly-serenity/stanford-ner.jar')
print(st.tag("I love to eat food at Stanford University with Professor John Smith".split()))
