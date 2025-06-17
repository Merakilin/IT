import subprocess
import argparse

def create_user_and_db(username="myuser", password="mypassword", dbname="mydb"):
    """Создает пользователя и базу данных PostgreSQL на Astra Linux."""

    try:
        # 1. Создание пользователя PostgreSQL
        try:
            subprocess.run(["sudo", "-u", "postgres", "psql", "-c", f"CREATE USER {username} WITH PASSWORD '{password}' SUPERUSER;"], check=True)
            print(f"Пользователь {username} успешно создан.")
        except subprocess.CalledProcessError as e:
            if "already exists" in str(e):
                print(f"Пользователь {username} уже существует, пропуск создания.")
            else:
                raise

        # 2. Создание базы данных PostgreSQL
        try:
            subprocess.run(["sudo", "-u", "postgres", "psql", "-c", f"CREATE DATABASE {dbname} OWNER {username};"], check=True)
            print(f"База данных {dbname} успешно создана.")
        except subprocess.CalledProcessError as e:
            if "already exists" in str(e):
                print(f"База данных {dbname} уже существует, пропуск создания.")
            else:
                raise

        print("Пользователь и база данных PostgreSQL успешно созданы.")

    except subprocess.CalledProcessError as e:
        print(f"Ошибка при создании пользователя и базы данных PostgreSQL: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Создание пользователя и базы данных PostgreSQL")
    parser.add_argument("--username", default="myuser", help="Имя пользователя PostgreSQL")
    parser.add_argument("--password", default="mypassword", help="Пароль пользователя PostgreSQL")
    parser.add_argument("--dbname", default="mydb", help="Имя базы данных")
    args = parser.parse_args()

    create_user_and_db(username=args.username, password=args.password, dbname=args.dbname)
