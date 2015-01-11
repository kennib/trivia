import db.models as User

def game_handler(request):
    request.write("""<!DOCTYPE html>
<html>
<body>

<h1>
01000111011000010110110101100101!!!
</h1>

<form method="post">

<br>
<label>Enter Player 1 (Username):</label>
<input type="text" name="username">
<br>

<label>Category:</label>
<input type="text" name="category">
<br>

<label>Difficulty:</label>
<input type="text" name="difficulty">

<br>
<input type="submit" value="Submit">
</form>

</body>
</html>
""")

def game_handler_post(request):

    if username == None or username == '' or password == None or password == '':
        request.redirect("/") #Says that the user is missing a feild
        return
