from core.engine import Engine
from rich.console import Console
from rich.table import Table

def run_dashboard(target):
    console = Console()
    console.rule("CI/CD Simulation")
    engine = Engine()
    engine.run(target)