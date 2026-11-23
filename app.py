
from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

number = random.randint(1, 100)
attempts = 0

html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Guess The Number</title>

    <style>
        body {
            background: #101020;
            color: white;
            text-align: center;
            font-family: Arial;
            padding: 40px 15px;
        }

        .game {
            background: #202040;
            padding: 25px;
            border-radius: 20px;
            max-width: 350px;
            margin: auto;
        }

        input {
            padding: 12px;
            width: 80%;
            border-radius: 10px;
            border: none;
            font-size: 18px;
        }

        button {
            padding: 12px 20px;
            margin: 10px;
            background: #00e5ff;
            border: none;
            border-radius: 10px;
            font-weight: bold;
        }

        h1 {
            color: #00e5ff;
        }

        .creator {
            color: #00e5ff;
            font-size: 13px;
            margin-top: 30px;
            opacity: 0.8;
        }
    </style>
</head>

<body>
    <div class="game">

        <h1>GUESS THE NUMBER</h1>

        <p>Guess a number between 1 and 100</p>

        <form method="POST">
            <input type="number" name="guess"
                   min="1" max="100" required>
            <br>
            <button type="submit">GUESS</button>
        </form>

        <h2>{{ message }}</h2>

        <p>Attempts: {{ attempts }}</p>

        <form method="POST">
            <button name="restart" value="yes">
                RESTART
            </button>
        </form>

        <p class="creator">ساخته شده توسط DS</p>

    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    global number, attempts

    message = "Let's Play!"

    if request.method == "POST":

        if request.form.get("restart"):
            number = random.randint(1, 100)
            attempts = 0
            message = "New Game!"

        else:
            guess = int(request.form["guess"])
            attempts += 1

            if guess > number:
                message = "Too High!"

            elif guess < number:
                message = "Too Low!"

            else:
                message = "YOU WIN!"

    return render_template_string(
        html,
        message=message,
        attempts=attempts
    )

app.run(host="0.0.0.0", port=5000)
