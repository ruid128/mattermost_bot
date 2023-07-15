import openai

openai.api_key = 'OPENAI_API_KEY'


def get_code_explanation(code):
    explanation = openai.Completion.create(
        engine='davinci-codex',
        prompt=f"Explain the following code:\n```\n{code}\n```",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return explanation.choices[0].text.strip()


def find_code_error(code):
    error = openai.Completion.create(
        engine='davinci-codex',
        prompt=f"Find the error in the following code:\n```\n{code}\n```",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return error.choices[0].text.strip()


def shorten_text(text):
    shortened_text = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Shorten the following text:\n```\n{text}\n```",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return shortened_text.choices[0].text.strip()


def paraphrase_text(text):
    paraphrased_text = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Paraphrase the following text:\n```\n{text}\n```",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return paraphrased_text.choices[0].text.strip()


def optimize_query(query):
    optimized_query = openai.Completion.create(
        engine='davinci',
        prompt=f"Optimize the following query:\n```\n{query}\n```",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return optimized_query.choices[0].text.strip()


def process_file_content(file_path, questions):
    with open(file_path, 'rb') as file:
        file_content = file.read().decode('utf-8')

    # Генерация ответов на вопросы
    generated_answers = []
    for question in questions:
        prompt = f"Question: {question}\nFile Content: {file_content}\nAnswer:"
        response = openai.Completion.create(
            engine='davinci',
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        answer = response.choices[0].text.strip()
        generated_answers.append(f"Q: {question}\nA: {answer}\n")

    return "\n".join(generated_answers)
