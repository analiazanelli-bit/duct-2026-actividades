import os
import pytest

# Importamos la función desde nuestro archivo analizador
# (Asegúrate de que tu analizador.py esté en la misma carpeta en Colab)
from analizador import contar_frecuencias


def test_conteo_basico(tmp_path):
  # Creamos un archivo temporal con texto de prueba
  archivo_prueba = tmp_path / "prueba_basica.txt"
  archivo_prueba.write_text("hola mundo hola", encoding="utf-8")

  resultado = contar_frecuencias(str(archivo_prueba))

  # Verificamos que 'hola' aparezca 2 veces y 'mundo' 1 vez
  assert resultado.get("hola") == 2
  assert resultado.get("mundo") == 1


def test_texto_vacio(tmp_path):
  # Creamos un archivo vacío
  archivo_prueba = tmp_path / "prueba_vacia.txt"
  archivo_prueba.write_text("", encoding="utf-8")

  resultado = contar_frecuencias(str(archivo_prueba))

  # Debe devolver un diccionario vacío
  assert resultado == {}


def test_mayusculas_y_minusculas(tmp_path):
  # Creamos un archivo con la misma palabra en mayúscula y minúscula
  archivo_prueba = tmp_path / "prueba_mayus.txt"
  archivo_prueba.write_text("Python PYTHON python", encoding="utf-8")

  resultado = contar_frecuencias(str(archivo_prueba))

  # Todas deberían agruparse bajo la clave en minúscula con un total de 3
  assert resultado.get("python") == 3