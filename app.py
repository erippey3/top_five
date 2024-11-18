from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Simple in-memory storage for submissions
submissions = []
submission_id_counter = 1

@app.route("/", methods=["GET", "POST"])
def home():
    global submissions, submission_id_counter
    if request.method == "POST":
        # Get the category and top five items from the form
        category = request.form.get("category", "").strip()
        items = [
            request.form.get(f"item{i}", "").strip() for i in range(1, 6)
        ]
        # Validate that all inputs are filled
        if category and all(items):
            submissions.append({
                "id": submission_id_counter,
                "category": category,
                "five": items
            })
            submission_id_counter += 1
        return redirect("/")
    return render_template("index.html", submissions=submissions)

@app.route('/delete/<int:submission_id>', methods=['POST'])
def delete_submission(submission_id):
    global submissions
    submissions = [s for s in submissions if s['id'] != submission_id]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
