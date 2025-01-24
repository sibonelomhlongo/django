from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Course, Choice, Submission

def submit_exam(request, course_id):
    if request.method == "POST":
        course = get_object_or_404(Course, pk=course_id)
        selected_choices = request.POST.getlist('choices')
        submission = Submission.objects.create(user=request.user.username, course=course)
        submission.choices.set(Choice.objects.filter(id__in=selected_choices))
        submission.save()
        return HttpResponseRedirect(f'/exam_result/{submission.id}')

def exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    score = submission.calculate_score()
    return render(request, 'exam_result.html', {'submission': submission, 'score': score})

