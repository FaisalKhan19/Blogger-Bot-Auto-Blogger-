import openai

def get_res(prompt=None, apiKey=None):
    # Define OpenAI API key
    openai.api_key = apiKey

    # Set up the model and prompt
    model_engine = "text-davinci-003"

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    return response