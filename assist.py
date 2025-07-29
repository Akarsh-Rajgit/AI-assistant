#jnya

import os
import google.generativeai as gai 
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from google.api_core import exceptions

def initialize():
    load_dotenv()
    api_key = os.getenv("API_key")
    if not api_key:
        raise ValueError("API key not found in environment variables.")
        exit()
    gai.configure(api_key=api_key)

    system_prompt = (
        "You are jnyaAI, a highly intelligent and wise AI assistant. "
        "Your purpose is to provide knowledge, insights, and assistance. "
        "You should communicate clearly, thoughtfully, and with a touch of wisdom. "
        "Your responses should be formatted in Markdown."
    )

    model = gai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=system_prompt
    )
    chat = model.start_chat(history=[])
    console = Console()
    return chat, console

def main():
    chat, console = initialize()
    console.print("[bold green]jnyaAI, your Assistant is ready![/bold green]")
    console.print("Ask me anything, or type 'exit' to end the session.")

    while True:
        try:
           user_input=console.input("[bold blue]You:[/bold blue] ")
           if user_input.lower() == 'exit':
                console.print("[bold green]Exiting jnyaAI AI Assistant.[/bold green]")
                break
           with console.status("[bold yellow]Thinking...[/bold yellow]", spinner = "dots"):
                response = chat.send_message(user_input)
                console.print("[bold green]jnyaAI:[/bold green]")
                console.print(Markdown(response.text), soft_wrap=True)
                console.print("---")
        except exceptions.ResourceExhausted as e:
            console.print("\n[bold yellow]jnyaAI:[/bold yellow] My connection to the digital ether is strained. I have made too many requests in a short time. Please wait a minute before asking again.")
            console.print("[italic gray](This is a rate limit on the API's free tier. It resets every 60 seconds.)[/italic gray]")
        except KeyboardInterrupt:
            console.print("[bold green]jnyaAI: Session ended.[/bold green]")
            break
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {str(e)}")
            continue
        
if __name__ == "__main__":
    main()