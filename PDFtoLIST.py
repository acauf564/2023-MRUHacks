import openai
import os
import time
from PyPDF2 import PdfReader

openai.api_key = "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"


def read_file():
    reader = PdfReader("sample_syllabus.pdf")
    number_of_pages = len(reader.pages)
    text = "<Please give me a python 2d list of all assignments, their due dates and percentage weights. If there is no due date or assignment weight, leave the field as an empty string. : "
    for i in range(number_of_pages):
        page = reader.pages[i]
        text += page.extract_text()
    formatted_contents = f'{text}>'
    return formatted_contents


def get_completion(prompt, model="gpt-3.5-turbo"):

    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message["content"]


prompt = read_file()
response = get_completion(prompt)

print(response)
