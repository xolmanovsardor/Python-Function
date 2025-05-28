tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Vazifa qo'shish")
    print("2. Vazifalarni ko'rish")
    print("3. Vazifani o'chirish")
    print("4. Chiqish")

def add_task():
    task = input("Yangi vazifani kiriting: ")
    tasks.append(task)
    print(f"✅ '{task}' vazifasi qo'shildi.")

def show_tasks():
    if not tasks:
        print("❌ Vazifalar yo'q.")
    else:
        print("\n📋 Vazifalar:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task():
    show_tasks()
    if tasks:
        try:
            index = int(input("O'chirmoqchi bo'lgan vazifa raqamini kiriting: "))
            removed = tasks.pop(index - 1)
            print(f"🗑️ '{removed}' o'chirildi.")
        except (IndexError, ValueError):
            print("❌ Noto‘g‘ri raqam.")

def run():
    while True:
        show_menu()
        choice = input("Tanlovni kiriting (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("👋 Dasturdan chiqildi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov.")

run()
