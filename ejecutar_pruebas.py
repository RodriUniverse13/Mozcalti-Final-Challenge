import pytest
import subprocess

def run_tests():
    # Ejecutar pytest y generar resultados en el directorio allure-results
    pytest.main(['--alluredir=allure-results'])

    # Generar y servir el reporte de Allure
    subprocess.run(['allure', 'serve', 'allure-results'])

if __name__ == "__main__":
    run_tests()