from flask import Flask, request, session
import io
import contextlib
import builtins
import os

import run  # this imports your run.py

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-me")  # Render env var recommended


def play_with_inputs(user_text: str):
    """
    Runs your existing run.hangman() but fakes input() using lines from user_text.
    Captures print() output and returns it as a string.
    """
    lines = (user_text or "").splitlines()
    idx = 0

    def fake_input(prompt=""):
        nonlocal idx
        if idx >= len(lines):
            # If the game asks for more input than we have, stop gracefully.
            raise EOFError
        value = lines[idx]
        idx += 1
        return value

    buf = io.StringIO()
    old_input = builtins.input
    builtins.input = fake_input
    try:
        with contextlib.redirect_stdout(buf):
            run.hangman()
    except EOFError:
        # Means: game asked for more input than provided; that's OK, we show partial output.
        pass
    finally:
        builtins.input = old_input

    return buf.getvalue()


@app.get("/")
def home():
    return """
    <h1>The Hangman Madness (Render)</h1>
    <p>Paste your inputs, one per line (username, level, category, guesses...).</p>
    <form method="post" action="/play">
      <textarea name="inputs" rows="12" cols="60"></textarea><br/>
      <button type="submit">Play</button>
    </form>
    """


@app.post("/play")
def play():
    user_text = request.form.get("inputs", "")
    output = play_with_inputs(user_text)
    return f"<pre>{output}</pre><p><a href='/'>Back</a></p>"
