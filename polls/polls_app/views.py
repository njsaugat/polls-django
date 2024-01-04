from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404
from .models import Question
from django.core.serializers import serialize
from polls.responses import CustomResponse;
def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")[:5]
    data = {"questions": [q.question_text for q in latest_question_list]}
    return JsonResponse(data)    # return Response(output,safe=False)


def getJsonData(givenField):
    return {field: getattr(givenField,field) for field in [f.name for f in givenField._meta.fields] if field!='_state'}
def detail(request,question_id):    
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        response=CustomResponse(status_code=404,status='Error',message="Question doesn't exist.",data=None)
        return JsonResponse(response.get_response())
    question_data=getJsonData(question)
    response=CustomResponse(status_code=200,status='Success',message="Question fetched successfully.",data={'question':question_data})
    return JsonResponse(response.get_response())


def results(request,question_id):
    response=f"You're looking at the resutls of {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"Your're voting on question {question_id}")