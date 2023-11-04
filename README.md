# OptimalQuest_Objective-Questions-with-Multiple-Correct-Answers (Creation of Objective Questions with Multiple Correct Answers)

Welcome to OptimalQuest, an innovative project designed to convert text content from PDF files into engaging multiple-choice questions with multiple correct answers.

## Features

- Extract text from PDFs.
- Generates multiple-choice questions.
- Each question can have multiple correct answers.
- Utilizes machine learning and natural language processing for question generation.

## Installation

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

1. Clone the repository: `git clone https://github.com/ShreeKeshavan/OptimalQuest_Objective-Questions-with-Multiple-Correct-Answers.git`
2. Install required libraries: `pip install spacy PyPDF2`

## Libraries Used 

- `Spacy`: For natural language processing tasks.
- `Random`: To generate randomness for question generation.
- `PyPDF2`: To read PDF files.
- `Warnings`: To suppress warnings.

## How to Use

1. Load the English language model using Spacy.

    ```python
    import spacy
    nlp_model = spacy.load("en_core_web_sm")
    ```
2. Extracting Text from PDFs: The `extract_text_from_pdfs` function is used to extract text from one or more PDF documents and concatenate it into a single text string. This is done using the `PdfReader` object from the `PyPDF2` library. Each page from each PDF is read and the text is extracted and appended to the output string.

   Here is an example of how to use this function:

   ```python
   # Define the PDF documents to extract text from
   pdf_files = ['chapter-2.pdf', 'chapter-3.pdf', 'chapter-4.pdf']

   # Extract text
   extracted_text = extract_text_from_pdfs(pdf_files)
   ```
3. Call the `get_mca_questions` function with the extracted text from the PDF and the number of questions as arguments. This will generate a list of multiple-choice questions.

    ```python
    get_mca_questions(text_context, num_of_questions)
    ```
