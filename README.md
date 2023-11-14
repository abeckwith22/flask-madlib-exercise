### Flask Madlib Exercise

`app.py`
```python
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
    
```

`stories.py`

The only thing that was modified about this file was getters so I could access prompts
```python
"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

    def getPrompts(self): # ['place', 'noun', 'verb', 'adjective', 'plural_noun']
        return self.prompts
    
    def getTemplate(self):
        return self.template

```
