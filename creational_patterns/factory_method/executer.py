from creator import Creator, CreatorConcreteOne, CreatorConcreteTwo


def client_code(creator: Creator) -> None:
    print(f"Client, No conozco la clase del creador, pero funciona")
    print(f"{creator.any_operation()}")


if __name__ == "__main__":
    print("App: Create with  CreatorConcreteOne.")
    client_code(CreatorConcreteOne())
    print("-----------------")

    print("App: Create with  CreatorConcreteTwo.")
    client_code(CreatorConcreteTwo())
