from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Submission(models.Model):
    user = models.CharField(max_length=100)  # Replace with `ForeignKey(User)` for authenticated users.
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def calculate_score(self):
        correct_answers = self.choices.filter(is_correct=True).count()
        total_questions = self.course.questions.count()
        return f"{correct_answers} / {total_questions}"
