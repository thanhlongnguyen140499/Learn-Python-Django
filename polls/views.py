from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.template import context
from .models import Question, Choice
from django.shortcuts import get_object_or_404

# Create your views here.
# display the latest 5 poll question
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    #     context = {'question': question}
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    # question = get_list_or_404(Question, pk=question_id)
    # context = {'question': question}
    # return render(request, 'polls/detail.html', context)

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    

def results(request, question_id):
    response = ("You are looking at the results of question %s. ")
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Youre voting on question %s." % question_id)
