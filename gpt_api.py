from flask import Flask, request, jsonify
import openai
import  book_locator
app = Flask(__name__)

# Set up OpenAI GPT credentials
openai.api_key = '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'

@app.route('/recommend', methods=['POST'])
def recommend_books():
    data = request.json
    user_input = data["message"]

    # Generate book recommendations using GPT
    prompt = "I'm looking for book recommendations. " + user_input + "Provide me with a json format with title and author"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=3,  # Number of recommendations to generate
        temperature=0.7  # Controls the randomness of the generated text
    )

    generated_recommendations = response.choices
    # print(generated_recommendations)
    recommended_books = []

    # Extract book titles from the generated text
    for recommendation in generated_recommendations:
        print(recommendation)
        book_title = recommendation.text.strip()
        recommended_books.append(book_title)
    print(recommended_books)
    # return book_locator.locate_book(jsonify({'recommendations': recommended_books}))
    return jsonify({'recommendations': recommended_books})


if __name__ == '__main__':
    app.run()
