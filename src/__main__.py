# Trace: T014
from src.store.in_memory_task_store import InMemoryTaskStore
from src.services.task_service import TaskService
from src.cli.commands import CLI


def main():
    store = InMemoryTaskStore()
    service = TaskService(store)
    cli = CLI(service)

    # simple loop for demonstration purposes
    print("Todo CLI — commands: add <title>|list|update <id> <title>|toggle <id>|delete <id>|exit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting")
            break
        if not raw:
            continue
        parts = raw.split(maxsplit=2)
        cmd = parts[0].lower()
        if cmd == "exit":
            print("Exiting")
            break
        if cmd == "add":
            title = parts[1] if len(parts) > 1 else ""
            description = parts[2] if len(parts) > 2 else None
            print(cli.add(title=title, description=description))
        elif cmd == "list":
            print(cli.list())
        elif cmd == "update":
            if len(parts) < 3:
                print("Usage: update <id> <title>")
                continue
            try:
                task_id = int(parts[1])
            except ValueError:
                print("ID must be an integer")
                continue
            new_title = parts[2]
            print(cli.update(task_id=task_id, title=new_title))
        elif cmd == "toggle":
            if len(parts) < 2:
                print("Usage: toggle <id>")
                continue
            try:
                task_id = int(parts[1])
            except ValueError:
                print("ID must be an integer")
                continue
            print(cli.toggle(task_id=task_id))
        elif cmd == "delete":
            if len(parts) < 2:
                print("Usage: delete <id>")
                continue
            try:
                task_id = int(parts[1])
            except ValueError:
                print("ID must be an integer")
                continue
            print(cli.delete(task_id=task_id))
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
