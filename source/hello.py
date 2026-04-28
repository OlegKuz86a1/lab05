"""CLI-утилита для приветствия пользователя с поддержкой формального стиля."""
# Импортируем typer для создания CLI с автогенерацией справки и валидацией типов аргументов
import typer

def main(
    name: str = typer.Option("AppSec Student", "--name", "-n", help="Имя пользователя."),
    lastname: str = typer.Option("", "--lastname", "-l", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
) -> None:
    """
    Выводит приветствие на основе переданных аргументов.
    :param name: Имя пользователя
    :param lastname: Фамилия пользователя
    :param formal: Флаг формального стиля
    """
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(main)
