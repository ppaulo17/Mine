# --- ARCHIVO 1: main.py ---
# Este es el punto de entrada. Ejecuta este archivo para probar tu bot.

import RPS_game
import RPS
from RPS_game import play, quincy, abbey, kris, mrugesh
import test_module

# 1. Prueba jugando contra Quincy
print("--- Jugando contra Quincy ---")
play(RPS.player, quincy, 1000)

# 2. Prueba jugando contra Abbey
print("\n--- Jugando contra Abbey ---")
play(RPS.player, abbey, 1000)

# 3. Prueba jugando contra Kris
print("\n--- Jugando contra Kris ---")
play(RPS.player, kris, 1000)

# 4. Prueba jugando contra Mrugesh
print("\n--- Jugando contra Mrugesh ---")
play(RPS.player, mrugesh, 1000)

# 5. Ejecutar las pruebas unitarias automáticas para verificar si pasas el examen
print("\n--- Ejecutando Unit Tests ---")
# Descomenta la siguiente línea para ejecutar los tests automáticamente
test_module.run_test()