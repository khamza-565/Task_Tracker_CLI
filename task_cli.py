import sys
import os
import json
from datetime import datetime


VALID_STATUSES = ["to-do", "in-progress", "done"]





def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []




def add_task(description):
    created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    tasks = load_tasks()
    if tasks:
        task_id = max(task["id"] for task in tasks) + 1
    else:
        task_id = 1
    tasks.append(
        {
            "id": task_id,
            "description": description,
            "status": "to-do",
            "createdAt": created_at,
            "updatedAt": created_at
        }
    )
    save_tasks(tasks)
    return tasks


def delete_task(task_id):
    tasks = load_tasks()
    old_count = len(tasks)
    tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) < old_count:
        save_tasks(tasks)
        return True
    else:
        return False


def update_task(task_id, new_description):
    created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = created_at
            save_tasks(tasks)
            return True
    return False



def update_status(task_id, new_status):
    created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    if new_status not in VALID_STATUSES:
        return False

    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = created_at
            save_tasks(tasks)
            return True
    return False



def list_tasks(task_status):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["status"] == task_status:
            found = True
            print(f"{task['id']} | Описание: {task['description']} "
                        f"| Статус: {task['status']} | Создано: {task['createdAt']} "
                        f"| Обновлено: {task['updatedAt']}")
    if not found:
        print("Задач с таким статусом не нашлось.")



def list_incomplete():
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["status"] != 'done':
            found = True
            print(f"{task['id']} | Описание: {task['description']} "
                        f"| Статус: {task['status']} | Создано: {task['createdAt']} "
                        f"| Обновлено: {task['updatedAt']}")
    if not found:
        print("Задач с таким статусом не нашлось.")





try:
    if len(sys.argv) < 2:
        print("Не указана команда")
    elif sys.argv[1] == "add":
        if len(sys.argv) < 3:
            print("Ошибка: укажите описание задачи.")
        else:
            description = sys.argv[2].strip()
            if description == "":
                print("Ошибка: описание задачи не может быть пустым.")
            else:
                add_task(description)
                print(f"Задача '{description}' добавлена")




    elif sys.argv[1] == "list":

        if len(sys.argv) > 3:
            print("Ошибка: укажите только один статус.")

        elif len(sys.argv) == 2:
            tasks = load_tasks()

            if not tasks:
                print("Задач пока нет.")
            else:
                for task in tasks:
                    print(
                        f"{task['id']} | Описание: {task['description']} "
                        f"| Статус: {task['status']} | Создано: {task['createdAt']} "
                        f"| Обновлено: {task['updatedAt']}"
                    )

        else:
            task_status = sys.argv[2].strip()

            if task_status == "":
                print("Ошибка: Название статуса не может быть пустым.")

            elif task_status in VALID_STATUSES:
                list_tasks(task_status)

            elif task_status == "incomplete":
                list_incomplete()

            else:
                print("Такого статуса нет")




    elif sys.argv[1] == "delete":
        if len(sys.argv) < 3:
            print("Ошибка: укажите ID задачи")
        elif sys.argv[2].strip() == "":
            print("Ошибка: ID задачи не может быть пустым.")
        elif not sys.argv[2].isdigit():
            print("Ошибка: ID должен быть числом.")
        else:
            task_id = int(sys.argv[2])
            if task_id <= 0:
                print("Ошибка: ID должен быть числом больше 0.")
            else:
                if delete_task(task_id):
                    print(f"Задача с ID {task_id} удалена.")
                else:
                    print(f"Ошибка: задача с ID {task_id} не найдена.")




    elif sys.argv[1] == "update":
        if len(sys.argv) < 4:
            print("Ошибка: Описание задачи не указано")
        elif sys.argv[2].strip() == "":
            print("Ошибка: ID задачи не может быть пустым.")
        elif sys.argv[3].strip() == "":
            print("Ошибка: Значение задачи не может быть пустым.")
        elif not sys.argv[2].isdigit():
            print("Ошибка: ID должен быть числом.")
        else:
            task_id = int(sys.argv[2])
            if task_id <= 0:
                print("Ошибка: ID должен быть числом больше 0.")
            else:
                new_description = sys.argv[3].strip()
                if update_task(task_id, new_description):
                    print(f"Задача {task_id} изменена на {new_description}.")
                else:
                    print(f"Ошибка: задача с ID {task_id} не найдена.")





    elif sys.argv[1] in ("mark-in-progress", "mark-done"):
        if len(sys.argv) < 3:
            print("Ошибка: ID задачи не указан")
        elif sys.argv[2].strip() == "":
            print("Ошибка: ID задачи не может быть пустым.")
        elif not sys.argv[2].isdigit():
            print("Ошибка: ID должен быть числом.")
        else:
            task_id = int(sys.argv[2])

            if task_id <= 0:
                print("Ошибка: ID должен быть числом больше 0!")
            else:

                if sys.argv[1] == "mark-in-progress":
                    new_status = "in-progress"
                else:
                    new_status = "done"

                tasks = load_tasks()
                description = None

                for task in tasks:
                    if task["id"] == task_id:
                        description = task["description"]
                        break

                if description is None:
                    print(f"Ошибка: задача с ID {task_id} не найдена.")
                elif update_status(task_id, new_status):
                    print(f"Статус задачи '{description}' изменён на '{new_status}'")
                else:
                    print("Ошибка: не удалось изменить статус задачи.")




    else:
        print(f"Неизвестная команда: {sys.argv[1]}")
except json.decoder.JSONDecodeError:
    print("Ошибка: файл tasks.json содержит некорректный JSON")







