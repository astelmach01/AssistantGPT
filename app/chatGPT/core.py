import openai

MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0.5


class ChatGPT:
    @staticmethod
    def get_chat_response(prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant aimed at improving the daily life of people. An example "
                    "of what you do is figure out a grocery shopping list when prompted, and decide when "
                    "the user should go shopping based on their schedule",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=TEMPERATURE,
        )

        return response["choices"][0]["message"]["content"]
