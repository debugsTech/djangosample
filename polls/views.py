from django.http import HttpResponse

from .models import Question

def index(request):
   latest_question_list = Question.objects.orderby("-pub_date")[:5]
   output = ", ".join([q.question.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



