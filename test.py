from db_config import DBConfig
from prompt_reader import PromptReader

if __name__ == "__main__":
    # Example database configuration

    prompt_reader = PromptReader()

    try:
        # Example query to fetch a prompt by name
        prompt_name = "Ashok"
        prompt = prompt_reader.get_prompt_by_name(prompt_name)
        if prompt:
            print(f"Prompt for '{prompt_name}': {prompt}")
        else:
            print(f"No prompt found with the name '{prompt_name}'")
    finally:
        # Close connection after usage
        prompt_reader.close()
