import requests

def showTask():
    try:
        response = requests.get("http://127.0.0.1:8000/api/tasks")
        return response.json()
    except requests.exceptions.HTTPError as err:
        print("ERROR")
        raise SystemExit(err)
    except requests.exceptions.ConnectionError as err:
        print(f"ERROR :  {err}")
    except requests.exceptions.JSONDecodeError as err:
        print(f"ERROR JSONDecodeError :  {err}")
        
def create_task(task):
    try:
        response = requests.post("http://127.0.0.1:8000/api/tasks", json={"name": task})
        return response.json()
    except requests.exceptions.HTTPError as err:
        print("ERROR")
        raise SystemExit(err)
    except requests.exceptions.ConnectionError as err:
        print(f"ERROR :  {err}")
    except requests.exceptions.JSONDecodeError as err:
        print(f"ERROR JSONDecodeError :  {err}")

p_salir = True

while p_salir:
    print("=======MENU DE API=======\n 1. Mostrar tareas\n 2. Crear tarea\n 3. Salir")
    try:
        op = int(input("Ingresa opcion: "))
    except ValueError as e:
        op = 0

    if op == 1:
        data = showTask()
        for task in data:
            print(task)
    elif op == 2:
        t = input("Ingrese la tarea: ")
        data = create_task(t)
        for task in data:
            print(task)
    elif op == 3:
        p_salir = False
        print("---Adios---")
    else:
        print("---Opcion no existente---\n")

