def new_question_handler(request):
  question = request.get_field("question")
  correct_answer = request.get_field("correct_answer")
  wrong_answer_1 = request.get_field("wrong_answer_1")
  wrong_answer_2 = request.get_field("wrong_answer_2")
  wrong_answer_3 = request.get_field("wrong_answer_3")
  print(question, correct_answer, wrong_answer_1, wrong_answer_2, wrong_answer_3)
  
def new_question_form(request):
    request.write("""<!DOCTYPE html>
<html>
<body>
<h1>
New Question Form :)
</h1>
<form method="post">
Question:<br>
<input type="text" name="question">
<br>
Correct answer:<br>
<input type="text" name="correct_answer">
<br>
Wrong answer 1:<br>
<input type="text" name="wrong_answer_1">
<br>
Wromg answer 2:<br>
<input type="text" name="wrong_answer_2">
<br>
Wrong answer 3:<br>
<input type="text" name="wrong_answer_3">
<br><br>
<input type="submit" value="Submit">
</form>
</body>
</html>
""")

def get_question_handler(request, question_id):
  request.write("""<!DOCTYPE html>
<html>
<body>
<h1>
Edit Question Form
</h1>
<form method="post">
Question:<br>
<input type="text" name="question">
<br>
Correct answer:<br>
<input type="text" name="correct_answer">
<br>
Wrong answer 1:<br>
<input type="text" name="wrong_answer_1">
<br>
Wromg answer 2:<br>
<input type="text" name="wrong_answer_2">
<br>
Wrong answer 3:<br>
<input type="text" name="wrong_answer_3">
<br><br>
<input type="submit" value="Submit">
</form>
</body>
</html>
""")


def edit_question_handler(request, question_id):
  print("Edit Question Handler")
  pass
