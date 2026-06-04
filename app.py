from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# FIXED LAST LINES, indentation fix tha
genai.configure(api_key="AQ.Ab8RN6KCXj3L4YwnQVxRNV_v9xQFnMMVL0pdZVzW4JJOxm72NQ")


model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()

        country = data.get("country", "")
        committee = data.get("committee", "")

        prompt = f"""
You are a professional MUN research assistant.

Country: {country}
Committee: {committee}

Generate a structured briefing with:

1. Country Overview
2. Foreign Policy
3. Key Statistics
4. Major Allies
5. Major Opponents
6. Relevant International Agreements
7. Talking Points
8. Possible Solutions
9. Opening Speech (90 seconds)

Use clear headings and detailed information.
"""
        response = model.generate_content(prompt)

        return jsonify({
            "response": response.text
        })

    except Exception as e:
        return jsonify({
            "response": f"Error: {str(e)}"
        })         

if __name__ == "__main__":
    app.run(debug=True, port=8000)
