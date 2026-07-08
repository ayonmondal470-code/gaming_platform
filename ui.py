from rich.console import Console
from rich.panel import Panel

console = Console()

def logo():
    console.print(
        Panel.fit(
            "[bold cyan]🎮 PYTHON GAMING PLATFORM 🎮[/bold cyan]\n"
            "[green]Made with Python + Termux[/green]",
            border_style="blue"
        )
    )

def menu():
    console.print("[yellow]1.[/yellow] Login")
    console.print("[yellow]2.[/yellow] Register")
    console.print("[yellow]3.[/yellow] Guess Number")
    console.print("[yellow]4.[/yellow] Rock Paper Scissors")
    console.print("[yellow]5.[/yellow] Tic Tac Toe")
    console.print("[yellow]6.[/yellow] Score Board")
    console.print("[yellow]7.[/yellow] Exit")


 from ui import logo, menu

         logo()
menu()



from rich.progress import track
import time

def loading():
    for _ in track(range(100), description="Loading Gaming Platform..."):
        time.sleep(0.02)





from ui import logo, menu, loading




loading()
logo()
