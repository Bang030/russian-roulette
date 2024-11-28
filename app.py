from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

# Game state variables
bullets_left = 6
bullet_position = random.randint(0, 5)
current_position = 0


@app.route("/")
def home():
    global bullets_left
    return render_template("index.html", bullets_left=bullets_left)


@app.route("/shoot")
def shoot():
    global bullets_left, bullet_position, current_position
    if bullets_left <= 0:
        return redirect(url_for("reset_game"))

    if current_position == bullet_position:
        return render_template("result.html", result="Bang! You died!")
    else:
        bullets_left -= 1
        current_position = (current_position + 1) % 6
        return redirect(url_for("home"))


@app.route("/reset")
def reset_game():
    global bullets_left, bullet_position, current_position
    bullets_left = 6
    bullet_position = random.randint(0, 5)
    current_position = 0
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
