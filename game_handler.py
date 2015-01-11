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
	username = request.get_field("username")
	category = request.get_field("category")
	difficulty = request.get_field("difficulty")
	
    if username is None or category is None or difficulty is None:
        request.redirect("/")
    
