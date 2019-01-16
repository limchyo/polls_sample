from django.db import models

# Create your models here.
class Question(models.Model):
    # 질문 데이터
    question_text = models.CharField(max_length=200)
    # 발행일(날짜/시각)
    pub_date = models.DateTimeField('date published')

    # 질문 내용 표기
    def __str__(self):
        return self.question_text

# 선택지
class Choice(models.Model):
    # 질문 가져오기
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 선택지 데이터
    choice_text = models.CharField(max_length=200)
    # 투표수(기본값 0)
    votes = models.IntegerField(default=0)

    # 선택지 내용 표기
    def __str__(self):
        return self.choice_text
