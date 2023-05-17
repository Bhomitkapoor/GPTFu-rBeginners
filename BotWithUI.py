import openai
import gradio

# Add your OpenAI - API KEY 
openai.api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'  # Add your API KEY

messages = [{"role": "system", "content": "You act as a Financial Advisor"}]

def customisedChatGPT(userInput):
    messages.append({"role": "user", "content": userInput})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    GPT_answer = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": GPT_answer})
    return GPT_answer


testingWithUI = gradio.Interface(
    fn=customisedChatGPT,     inputs=gradio.inputs.Textbox(
        lines=5, placeholder='Type your question here...'),
    outputs="text", title="Financial GuruJI",
    description="Ask any finance-related questions, and the AI will provide an answer.",
    theme='gradio/seafoam'
)

testingWithUI.launch(share=True)
