from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        answers = {
            "cpu": "central processing unit",
            "gpu": "graphics processing unit",
            "ram": "random access memory",
            "psu": "power supply"
        }

        user_answers = {
            "cpu": request.form.get('cpu').lower(),
            "gpu": request.form.get('gpu').lower(),
            "ram": request.form.get('ram').lower(),
            "psu": request.form.get('psu').lower()
        }

        for key in answers:
            if user_answers[key] == answers[key]:
                score += 1

        percentage = (score / len(answers)) * 100

        return render_template('quiz.html', score=score, percentage=percentage, submitted=True)

    return render_template('quiz.html', submitted=False)

if __name__ == '__main__':
    app.run(debug=True)
