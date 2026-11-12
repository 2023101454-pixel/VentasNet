# Registro de cambios

## INC-001: Error en el total con varias unidades

- **ID:** INC-001
- **Origen:** Incidencia detectada en el módulo de ventas
- **Descripción:** El total no considera la cantidad; la función devuelve solo el precio.
- **Justificación:** Los pedidos con varias unidades muestran un importe incorrecto.
- **Requisito afectado:** RF-001
- **Archivos involucrados:** src/ventas.py
- **Riesgo:** Total incorrecto en las ventas.
- **Criterio de aceptación:** Precio 50 × cantidad 3 = S/ 150.
- **Prioridad:** Alta
- **Decisión:** Aprobada (aprobación académica simulada)
- **Responsable:** Antony
- **Estado:** Implementada y verificada
- **Rama:** fix/INC-001-total
- **Prueba:** CP-001 (50 × 3 = S/ 150), aprobada

## CR-002: Descuento del 10 % desde S/ 200

- **ID:** CR-002
- **Origen:** Solicitud del área comercial
- **Descripción:** Aplicar 10 % de descuento cuando el subtotal sea igual o superior a S/ 200.
- **Justificación:** El área comercial quiere incentivar compras de mayor monto.
- **Requisito afectado:** RF-002 (nuevo)
- **Archivos involucrados:** src/ventas.py, docs/requisitos.md
- **Riesgo:** Descuento incorrecto en el umbral (subtotal justo en S/ 200).
- **Criterio de aceptación:** Subtotal 200 → S/ 180; subtotal 150 → S/ 150.
- **Prioridad:** Media
- **Decisión:** Aprobada (aprobación académica simulada)
- **Responsable:** Antony

## Matriz de impacto

| Criterio | INC-001 | CR-002 |
|---|---|---|
| Requisito | RF-001 | RF-002 (nuevo) |
| Archivo | src/ventas.py | src/ventas.py; docs/requisitos.md |
| Riesgo | Total incorrecto | Descuento incorrecto en umbral |
| Prueba | 50 × 3 = 150 | Subtotales 150, 200 y 300 |
| Decisión simulada | Aprobada | Aprobada |

## Justificación del impacto

- **INC-001:** Afecta al requisito RF-001, porque el total debe calcularse según precio y cantidad. Solo se modifica `src/ventas.py`. El riesgo es que se sigan mostrando totales incorrectos. Se verifica con la prueba 50 × 3 = 150.
- **CR-002:** Genera un requisito nuevo (RF-002), por lo que se actualiza `docs/requisitos.md` y se modifica `src/ventas.py`. El riesgo está en el umbral de S/ 200: un subtotal de 200 debe tener descuento y uno de 150 no. Se verifica con los subtotales 150, 200 y 300.
- **Decisión:** Ambas solicitudes se aprueban de forma simulada para fines académicos, y se atienden por separado en ramas distintas.

## Aprobación académica simulada

- **INC-001:** Aprobada. Se corregirá en la rama `fix/INC-001-total`.
- **CR-002:** Aprobada. Se implementará en la rama `feature/CR-002-descuento`.
- **Fecha:** 12/11/2026
- **Aprobado por:** Docente del curso (simulado)