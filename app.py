import builtins
import contextlib
import io
import os

from flask import Flask, request, render_template, render_template_string, url_for

import run  # your existing run.py (must contain hangman())


app = Flask(__name__, static_folder="static", template_folder="templates")
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
        # Means the game asked for more input than we provided.
        pass
    finally:
        builtins.input = old_input

    return buf.getvalue()


# --- Option 1 (recommended): use templates if they exist ---
# Create:
#   templates/index.html
#   templates/result.html
#
# And put your assets in:
#   static/style.css
#   static/app.js
#   static/image.png
#
# If templates are missing, the app will fall back to inline HTML below.
@app.get("/")
def home():
    if os.path.exists(os.path.join(app.template_folder, "index.html")):
        return render_template("index.html")
    return render_template_string(_home_inline_html())


@app.post("/play")
def play():
    user_text = request.form.get("inputs", "")
    output = play_with_inputs(user_text)

    if os.path.exists(os.path.join(app.template_folder, "result.html")):
        return render_template("result.html", output=output)

    return render_template_string(_result_inline_html(), output=output)


def _home_inline_html() -> str:
    # Uses url_for so paths always work.
    css = url_for("static", filename="style.css")
    js = url_for("static", filename="app.js")
    bg = url_for("static", filename="image.png")

    return f"""
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>The Hangman Madness</title>
    <link rel="stylesheet" href="{css}">
    <script defer src="{js}"></script>

    <!-- Fallback styles if style.css is missing -->
    <style>
      body {{
        margin:0;
        min-height:100vh;
        background-image:url("{bg}");
        background-size:cover;
        background-repeat:no-repeat;
        background-position:center;
        font-family: Arial, sans-serif;
      }}
      .card {{
        background: rgba(255,255,255,0.90);
        width: min(900px, 92%);
        margin: 40px auto;
        padding: 16px 20px;
        border-radius: 10px;
      }}
      textarea {{
        width: 100%;
        max-width: 100%;
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      }}
      button {{
        margin-top: 10px;
        padding: 10px 14px;
        cursor: pointer;
      }}
    </style>
  </head>

  <body>
    <div class="card">
      <h1>The Hangman Madness (Render)</h1>
      <p>Paste your inputs below, one per line (username, level, category, guesses...).</p>

      <form method="post" action="/play">
        <textarea name="inputs" rows="12" placeholder="Type/paste inputs here..."></textarea><br/>
        <button type="submit">Play</button>
      </form>
    </div>
  </body>
</html>
"""


def _result_inline_html() -> str:
    css = url_for("static", filename="style.css")
    js = url_for("static", filename="app.js")
    bg = url_for("static", filename="image.png")

    return f"""
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Hangman Output</title>
    <link rel="stylesheet" href="{css}">
    <script defer src="{js}"></script>

    <!-- Fallback styles if style.css is missing -->
    <style>
      body {{
        margin:0;
        min-height:100vh;
        background-image:url("{bg}");
        background-size:cover;
        background-repeat:no-repeat;
        background-position:center;
        font-family: Arial, sans-serif;
      }}
      .card {{
        background: rgba(255,255,255,0.90);
        width: min(1000px, 92%);
        margin: 40px auto;
        padding: 16px 20px;
        border-radius: 10px;
      }}
      pre {{
        white-space: pre-wrap;
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      }}
      a {{
        display:inline-block;
        margin-top:10px;
      }}
    </style>
  </head>

  <body>
    <div class="card">
      <pre>{{{{ output }}}}</pre>
      <a href="/">Back</a>
    </div>
  </body>
</html>
"""


if __name__ == "__main__":
    # Local testing only. On Render you run: gunicorn app:app
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
