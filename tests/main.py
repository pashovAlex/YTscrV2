from flask import Flask, render_template
import subprocess
import io
import sys
import contextlib

app = Flask(__name__)

@app.route('/')
def index():
    @contextlib.contextmanager
    def capture():
        out, err = io.StringIO(), io.StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = out, err
            yield out, err
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    with capture() as (out, err):
        command = "ls -l"  # Replace with your shell command
        subprocess.run(command, shell=True, stdout=out, stderr=err)

    output = out.getvalue()

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(port=8080)