import gzip
from Classes import Review

def parse(path):
  g = gzip.open(path, 'r')
  
  for l in g:
    temp = eval(l)
    print temp
    currentReview = Review(temp['questionType'], temp['asin'], temp['answerTime'], temp['unixTime'], temp['question'], temp['answerType'], temp['answer'])
    print currentReview.answer