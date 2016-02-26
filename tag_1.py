from nltk.tag.stanford import NERTagger

st = NERTagger('/Users/catherinaxu/Dropbox/Stanford/EC/Neighborly/neighborly-serenity/english.all.3class.distsim.crf.ser.gz','/Users/catherinaxu/Dropbox/Stanford/EC/Neighborly/neighborly-serenity/stanford-ner.jar')
pdf = open('output.1.txt')
for line in pdf:
    print(st.tag(line.split()))


