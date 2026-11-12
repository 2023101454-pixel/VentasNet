# Casos de prueba

## INC-001: Cálculo del total por cantidad

| Caso | Dato de entrada | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|
| CP-001 | Precio 50, cantidad 3 | S/ 150 | S/ 150 | Aprobado |

## CR-002: Descuento del 10 % desde S/ 200

| Caso | Dato de entrada | Subtotal esperado | Total esperado | Subtotal obtenido | Total obtenido | Estado |
|---|---|---|---|---|---|---|
| CP-002 | Precio 50, cantidad 3 | S/ 150 | S/ 150 | S/ 150 | S/ 150 | Aprobado |
| CP-003 | Precio 50, cantidad 4 | S/ 200 | S/ 180 | S/ 200 | S/ 180.0 | Aprobado |
| CP-004 | Precio 100, cantidad 3 | S/ 300 | S/ 270 | S/ 300 | S/ 270.0 | Aprobado |