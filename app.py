from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

prompts = story.getPrompts()
template = story.getTemplate()

@app.route('/')
def homepage():
    return render_template('homepage.html', prompts=prompts, template=template)


@app.route('/madlib')
def read_madlib():
    # answers = [i for i in prompts request.args[i]] trying to figure out shorthanded way of doing it
    answers = {}
    for i in prompts:
        answers[i] = request.args[i]
    
    generated_story = story.generate(answers)

    return render_template('madlibstory.html', story=generated_story)