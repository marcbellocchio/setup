from cx_Freeze import setup, Executable
setup(
        name = "Pings",
        version = "1.0",
        description = "utilitaire_reseau",
        executables = [Executable("Pings.py")])
