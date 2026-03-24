import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from call_functions import available_functions, call_function
def response_func(client, messages):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
            )
        )
    return response
def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user",parts=[types.Part(text=args.user_prompt)])]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not found. Make sure it's set in your .env file.")

    client = genai.Client(api_key=api_key)
    for i in range(20):
        response = response_func(client, messages)

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if not response.function_calls:
            print(response.text)
            return

        func_resp = []
        for func_call in response.function_calls:
            result = call_function(func_call, args.verbose)
            func_resp.append(result.parts[0])

        messages.append(types.Content(role="user", parts=func_resp))

    print("Maximum iterations reached")
        
    if response.usage_metadata == None:
        raise RuntimeError
    if args.verbose:
        print("User prompt: ", args.user_prompt)
        print("Prompt tokens: ",response.usage_metadata.prompt_token_count)
        print("Response tokens: ",response.usage_metadata.candidates_token_count)
    
    if response.function_calls:
        new_list = []
        for item in response.function_calls:
            result=call_function(item, args.verbose)
            if not result.parts:
                raise Exception("result.parts is empty")
            if not result.parts[0].function_response:
                raise Exception("result.parts[0].function_response is empty")
            if not result.parts[0].function_response.response:
                raise Exception (".parts[0].function_response.response is empty")
            new_list.append(result.parts[0])
            if args.verbose:
                print(f"-> {result.parts[0].function_response.response}")
    else:  
        print(response.text)

if __name__ == "__main__":
    main()

