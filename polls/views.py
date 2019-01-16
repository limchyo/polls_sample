from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Question, Choice

# Create your views here.
def index(request):
    # 저장된 질문 모두 가져온다
    # 내림차순으로 정렬 (최근 5개)
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    # 모든 객체 호출, 내림차순 정렬, 그 중 최근 객체 5개
    ctx = { "latest_question_list" : latest_question_list }
    return render(request, "index.html", ctx)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    ctx = { "question" : question }
    return render(request, "detail.html", ctx)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Question와 연결된 choice 객체와 연결
        # question.choice_set은 질문 속 선택지 객체를 말한다
        # choice.get()은 선택 받은 선택지이다
        # 따라서 폼을 통해 선택 받은 선택지를 인스턴스로 지정
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        # request.POST.get("choice")

    # 선택지 미선택 제출시 예외 처리
    except (KeyError, Choice.DoesNotExist):
        return render(request, "detail.html", {
            "question" : question,
            "error_message" : "You didn't select a choice.",
        })

    # 선택하고 제출한 경우
    else:
        # 투표수 데이터에 더하기 1을 하고 저장
        selected_choice.votes += 1
        selected_choice.save()
        # 해당 질문에 대한 결과페이지로 리다이렉트
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        ctx = { "question" : question }
        return render(request, "results.html", ctx)
