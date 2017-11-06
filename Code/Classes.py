class Review :

  def __init__(self, questionType, asin, answerTime, unixTime, question, answerType, answer):
    self.questionType = questionType
    self.asin = asin
    self.answerTime = answerTime
    self.unixTime = unixTime
    self.question = question
    self.answerType = answerType
    self.answer = answer

  def getQuestionType():
    return self.questionType

  def getAsin():
    return self.asin

  def getAnswerTime():
    return self.answerTime

  def getUnixTime():
    return self.unixTime

  def getQuestion():
    return self.question

  def getAnswerType():
    return self.answerType

  def getAnswer():
    return self.answer