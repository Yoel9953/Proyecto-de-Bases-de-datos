import subprocess


def export_backup() -> None:
    """
    Exporta la base de datos en texto plano usando pg_dump.
    Ajusta el usuario y el nombre de la base según tu configuración.
    """
    command = 'pg_dump -U postgres -d tienda_videojuegos > respaldo_tienda_videojuegos.sql'
    subprocess.run(command, shell=True, check=True)