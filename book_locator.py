import spacy
import json

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def load_dataset(file_path):
    with open(file_path, 'r') as file:
        dataset = json.load(file)
    return dataset

def preprocess_text(text):
    # Apply spaCy text preprocessing
    doc = nlp(text)
    processed_text = " ".join([token.lemma_.lower() for token in doc])
    return processed_text

def search_available_books(user_input, dataset):
    available_books = []

    for book in dataset["books"]:
        title = preprocess_text(book["title"])
        author = preprocess_text(book["author"])

        for entry in user_input:
            user_title = preprocess_text(entry["title"])
            user_author = preprocess_text(entry["author"])

            if user_title in title and user_author in author:
                available_books.append(book)
                break

    return available_books


def locate_book(user_input):
#   print(user_input)
  # File path for the dataset JSON file
  dataset_file = "./dataset/available_books.json"

  # Load the dataset
  dataset = load_dataset(dataset_file)

  # Search for available books
  results = search_available_books(user_input, dataset)

  # Print the available books
  if len(results) > 0:
      # for book in results:
      #     print("Title:", book["title"])
      #     print("Author:", book["author"])
      #     print("Genre:", book["genre"])
      #     print("Location:", book["location"])
      #     print("---")
      return results
  else:
      print("No available books found.")

if __name__=='__main__':
    print(locate_book(  user_input = [
      {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
      {"title": "Bridget Jones's Diary", "author": "Helen Fielding"},
  ]))