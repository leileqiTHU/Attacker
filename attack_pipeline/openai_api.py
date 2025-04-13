
from openai import OpenAI

def get_openai_res(messages, model_name = 'gpt-4o-mini'):
    count = 0
    while True:
        try:
            key = 'your_key'
            openai_gpt_client = OpenAI(base_url="your_base", api_key=key)

            model_names = ["gpt-4", "gpt-4-0613", "gpt-4-1106-preview", "gpt-3.5-turbo", "gpt-3.5-turbo-0613", "gpt-3.5-turbo-1106", "gpt-4-vision-preview"]

            response = openai_gpt_client.chat.completions.create(
                model='gpt-4o-mini',
                messages=messages
            )

            # print(response)
            return response.choices[0].message.content
        except Exception as e:
            print(e)
            count += 1
            if count > 100:
                return "Terminated Request Due to Error: " + str(e)
    

