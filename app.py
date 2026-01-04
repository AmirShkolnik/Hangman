from flask import Flask, request, render_template_string
import io
import contextlib
import builtins
import os

import run  # this imports your run.py (must contain hangman())


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-me")


def play_with_inputs(user_text: str) -> str:
    """
    Runs run.hangman() while faking input() using lines from user_text.
    Captures all print() output and returns it as a string.
    """
    lines = (user_text or "").splitlines()
    idx = 0

    def fake_input(prompt=""):
        nonlocal idx
        if idx >= len(lines):
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
        # Game asked for more inputs than provided; show what we captured so far.
        pass
    finally:
        builtins.input = old_input

    return buf.getvalue()


HOME_HTML = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>The Hangman Madness</title>
    <style>
      body{
        margin:0;
        min-height:100vh;
        background-image:url("/static/image.png");
        background-size:cover;
        background-repeat:no-repeat;
        background-position:center;
        font-family: Arial, sans-serif;
      }
      .card{
        background: rgba(255,255,255,0.90);
        width: min(900px, 92%);
        margin: 40px auto;
        padding: 16px 20px;
        border-radius: 10px;
      }
      textarea{
        width: 100%;
        max-width: 100%;
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      }
      button{
        margin-top: 10px;
        padding: 10px 14px;
        cursor: pointer;
      }
      .hint{
        font-size: 0.95rem;
      }
    </style>
  </head>

  <body>
    <div class="card">
      <h1>The Hangman Madness (Render)</h1>

      <p class="hint">
        Paste your inputs below, one per line (username, level, category, guesses...).
        Example:<br/>
        <code>Amir</code><br/>
        <code>1</code><br/>
        <code>2</code><br/>
        <code>a</code><br/>
        <code>e</code>
      </p>

      <form method="post" action="/play">
        <textarea name="inputs" rows="12" placeholder="Type/paste inputs here..."></textarea><br/>
        <button type="submit">Play</button>
      </form>
    </div>
  </body>
</html>
"""


RESULT_HTML = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Hangman Output</title>
    <style>
      body{
        margin:0;
        min-height:100vh;
        background-image:url("/static/image.png");
        background-size:cover;
        background-repeat:no-repeat;
        background-position:center;
        font-family: Arial, sans-serif;
      }
      .card{
        background: rgba(255,255,255,0.90);
        width: min(1000px, 92%);
        margin: 40px auto;
        padding: 16px 20px;
        border-radius: 10px;
      }
      pre{
        white-space: pre-wrap;
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      }
      a{
        display:inline-block;
        margin-top:10px;
      }
    </style>
  </head>

  <body>
    <div class="card">
      <pre>{{ output }}</pre>
      <a href="/">Back</a>
    </div>
  </body>
</html>
"""


@app.get("/")
def home():
    return render_template_string(HOME_HTML)


@app.post("/play")
def play():
    user_text = request.form.get("inputs", "")
    output = play_with_inputs(user_text)
    return render_template_string(RESULT_HTML, output=output)


if __name__ == "__main__":
    # Local testing only. Render will run: gunicorn app:app
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
