from nltk.tag.stanford import NERTagger

st = NERTagger('/Users/catherinaxu/Dropbox/Stanford/EC/Neighborly/neighborly-serenity/english.all.3class.distsim.crf.ser.gz','/Users/catherinaxu/Dropbox/Stanford/EC/Neighborly/neighborly-serenity/stanford-ner.jar')
print(st.tag("I love to eat food at Stanford University with Professor John Smith".split()))

