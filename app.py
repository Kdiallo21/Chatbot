from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

# Define the pairs of rules
set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me a chatbot."]
    ],
    [
        r"how are you?",
        ["I am fine, thank you! How can I help you?"]
    ],
    [
        r"I am fine, thank you",
        ["Great to hear that, how can I help you?"]
    ],
    [
        r"how can I help you?",
        [
            "I am looking for online guides and courses to learn data science. Can you suggest?",
            "I am looking for data science training platforms."
        ]
    ],
    [
        r"I'm (.*) doing good",
        ["That's great to hear.", "How can I help you? :)"]
    ],
    [
        r"I am looking for online guides and courses to learn data science, can you suggest?",
        ["Pluralsight is a great option to learn data science. You can check their website."]
    ],
    [
        r"thanks for the suggestion. Do they have great authors and instructors?",
        ["Yes, they have world-class authors. That is their strength ;)"]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["I am happy to help.", "No problem, you're welcome."]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
]

# Initialize Flask app
app = Flask(__name__)

# Define chatbot logic
chat = Chat(set_pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")  # Render the HTML template

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    bot_response = chat.respond(user_input)
    return bot_response or "I'm sorry, I didn't understand that."

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
