# JnyaAI 
import ollama
from rich.console import Console
from rich.markdown import Markdown

def initialize():
    console = Console()
    console.print("[bold green]JnyaAI: your Assistant (Local Edition)[/bold green]")
    console.print("Powered by a local model via Ollama(tinyllama). No internet required.")
    console.print("Ask me anything, or type 'exit' to end the session.")
    return console, [] 

def main():
    console, messages = initialize()
    messages.append({
        'role': 'system',
        'content': (
            "You are JnyaAI, a highly intelligent and wise AI assistant. "
            "Your purpose is to provide knowledge, insights, and assistance. "
            "You should communicate clearly, thoughtfully, and with a touch of wisdom."
        ),
    })

    while True:
        try:
            user_input = console.input("[bold blue]You: [/bold blue]")

            if user_input.lower() in ['exit', 'quit']:
                console.print("[bold green]JnyaAI: Farewell.[/bold green]")
                break

            messages.append({'role': 'user', 'content': user_input})

            full_response = ""
            with console.status("[bold green]JnyaAI is thinking...[/bold green]", spinner="dots"):
                stream = ollama.chat(
                    model='tinyllama', 
                    messages=messages,
                    stream=True,
                )
            
            console.print("\n[bold green]JnyaAI:[/bold green]", end="")
            for chunk in stream:
                part = chunk['message']['content']
                console.print(part, end="")
                full_response += part
            
            console.print("\n---")
            messages.append({'role': 'assistant', 'content': full_response})

        except KeyboardInterrupt:
            console.print("\n[bold green]JnyaAI: Session ended. Farewell.[/bold green]")
            break
        except Exception as e:
            console.print(f"[bold red]An error occurred: {e}[/bold red]")
            break

if __name__ == "__main__":
    main()
