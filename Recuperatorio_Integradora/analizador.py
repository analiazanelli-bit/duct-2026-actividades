def contar_frecuencias(ruta_archivo):
  """Lee un archivo de texto y devuelve un diccionario con la frecuencia

  de cada palabra.
  """
  frecuencias = {}

  try:
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
      for linea in archivo:
        # Pasamos todo a minúsculas y separamos por espacios
        palabras = linea.lower().split()

        for palabra in palabras:
          # Limpiamos signos de puntuación básicos que puedan pegarse a la palabra
          palabra = palabra.strip(".,;:()[]{}\"'-")

          if palabra:  # Si no quedó vacía
            # Si ya está en el diccionario, sumamos 1; si no, la inicializamos en 1
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

  except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{ruta_archivo}'.")

  return frecuencias


# Código de prueba para verificar que funcione
if __name__ == "__main__":
  resultado = contar_frecuencias("texto_integradora.txt")
  print("¡Conteo finalizado!")
  print("Primeras 5 palabras encontradas:", list(resultado.items())[:5])
