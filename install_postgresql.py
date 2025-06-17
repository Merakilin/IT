import subprocess

def install_postgresql(version="12"):
    """Устанавливает PostgreSQL на Astra Linux."""

    try:
        subprocess.run(["sudo", "apt", "update"], check=True)

        packages = ["postgresql", "postgresql-contrib"]
        subprocess.run(["sudo", "apt", "install"] + packages, check=True)

        subprocess.run(["sudo", "systemctl", "start", "postgresql"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "postgresql"], check=True)

        print("PostgreSQL успешно установлен и запущен!")

    except subprocess.CalledProcessError as e:
        print(f"Ошибка при установке PostgreSQL: {e}")

if __name__ == "__main__":
    install_postgresql()
