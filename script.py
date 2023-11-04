#Creation of Objective Questions with Multiple Correct Answers

"""Importing Libraries"""

import spacy
import random
from PyPDF2 import PdfReader

# To supress warnings
import warnings
warnings.filterwarnings("ignore")



"""Loading English Language Model"""

# Load English language model
nlp_model = spacy.load("en_core_web_sm")



"""Multiple Choice Question Generating Function"""

# Define a function to generate multiple-choice questions based on the provided text context and the number of questions desired.
def get_mca_questions(text_context: str, num_of_questions: int):
    # Process the text context using the NLP model and store it in the 'doc' variable.
    doc = nlp_model(text_context)

    # Define a function to create a multiple-choice question with multiple correct answers.
    def create_mcq_with_multiple_correct(question_text, correct_answers, other_options, num_options=4):
        # Combine correct answers and other options, then shuffle them.
        options = correct_answers + other_options
        random.shuffle(options)

        # Create a dictionary representing the multiple-choice question.
        mcq = {
            "question": question_text,  # The question text.
            "options": options,         # All answer options (shuffled).
            "correct_answers": correct_answers  # List of correct answer options.
        }

        return mcq

    # Define a function to generate a variety of questions.
    def generate_variety_question():
        # Select a random sentence from the processed document.
        random_sentence = random.choice(list(doc.sents))
        # Choose a random word within the sentence that is not a punctuation mark.
        random_word = random.choice([token for token in random_sentence if not token.is_punct])

        # Replace the selected word with "______" to create a blank in the question text.
        question_text = random_sentence.text.replace(random_word.text, "______")
        correct_answers = [random_word.text]  # List of correct answer options.

        # Create a list of other word options for the question.
        other_options = [token.text for token in doc if token.is_alpha and token.text != correct_answers[0]]
        num_correct_options = random.randint(1, 2)  # Generate 1 or 2 correct options.
        correct_answers.extend(random.sample(other_options, num_correct_options))

        num_other_options = min(4 - num_correct_options, len(other_options))
        # Randomly select additional word options to complete the multiple-choice options.
        other_options = random.sample(other_options, num_other_options)

        # Generate the multiple-choice question with correct options using the function defined earlier.
        mcq = create_mcq_with_multiple_correct(question_text, correct_answers, other_options)
        return mcq

    # Generate a list of questions based on user input.
    generated_questions = [generate_variety_question() for _ in range(num_of_questions)]

    # Initialize a list to store the final multiple-choice questions.
    mca_questions = []

    # Loop through the generated questions to format them and add to the list.
    for i, question in enumerate(generated_questions, start=1):
        question_str = f"Q{i}: {question['question']}\n"  # Format the question string.
        options_str = ""

        # Loop through the answer options to format them.
        for j, option in enumerate(question['options']):
            options_str += f"{j + 1}. {option}\n"

        # Format the correct answer options to include in the question.
        correct_options_formatted = " & ".join(f"({chr(97 + question['options'].index(ans))})" for ans in question['correct_answers'])
        correct_options_str = f"Correct Options: {correct_options_formatted}"

        # Combine the question, options, and correct options for the final question and add it to the list.
        mca_question = f"{question_str}{options_str}{correct_options_str}\n"
        mca_questions.append(mca_question)

    # Return the list of formatted multiple-choice questions.
    return mca_questions



"""Data Extraction Function"""

# Define a function to extract text from PDF documents and concatenate it into a single text string.
def extract_text_from_pdfs(pdf_documents):
    extracted_text = ""
    for pdf_file in pdf_documents:
        # Initialize the PDF reader to extract text from the current PDF document.
        pdf_reader = PdfReader(pdf_file)
        for pdf_page in pdf_reader.pages:
            # Concatenate the text from each page to the 'extracted_text' string.
            extracted_text += pdf_page.extract_text()
    return extracted_text

# Define the PDF documents to extract text from
pdf_file1 = 'chapter-2.pdf'
pdf_file2 = 'chapter-3.pdf'
pdf_file3 = 'chapter-4.pdf'

pdf_documents = [pdf_file1, pdf_file2, pdf_file3]
# Extract text from the specified PDFs and store it in 'document_text'
document_text = extract_text_from_pdfs(pdf_documents)
text_context = document_text



"""User Input"""

# Prompt the user to input the number of questions
number_of_questions = int(input("Enter the number of questions: "))

# Generate and display multiple-choice questions based on the extracted text
generated_questions = get_mca_questions(text_context, number_of_questions)
for question in generated_questions:
    print(question)