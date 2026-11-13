# Examen practico 3: Python

---

## Instrucciones

- El examen tiene **cinco preguntas**. Se deben responder **cuatro**; la pregunta restante queda como **comodín** y no se responde.
- Cada pregunta vale **2,5 puntos**. La puntuación máxima del examen es de **10 puntos**.
- Se corrige por resultado, no por procedimiento.
- Se debe entregar todo el examen en una única carpeta comprimida que debe llamarse siguiendo la convención: `Apellidos_Nombres.zip`.
- Las respuestas deben estar identificadas con su pregunta respectiva.
- Aparte del zip se debe entregar el enlace de grabación del examen.
- Se restarán puntos si se entrega con retraso y si no se cumplen las instrucciones: un punto menos por cada instrucción no cumplida y un punto menos por entregar con retraso.
- No se permiten entregas por chats privados; las entregas se hacen únicamente por la tarea creada para el examen.

---

## Pregunta 1 · Pedidos de una floristería (2,5 puntos)

Una floristería registra los pedidos de ramos que ha recibido hoy:

```python
pedidos = [
    {"codigo": "F01", "cliente": "Alba",  "ramos": 1, "importe": 25.00, "domicilio": True},
    {"codigo": "F02", "cliente": "Bruno", "ramos": 3, "importe": 54.00, "domicilio": False},
    {"codigo": "F03", "cliente": "Carla", "ramos": 2, "importe": 38.50, "domicilio": True},
    {"codigo": "F04", "cliente": "David", "ramos": 1, "importe": 15.00, "domicilio": False},
    {"codigo": "F05", "cliente": "Elena", "ramos": 4, "importe": 72.00, "domicilio": True},
]
```

A los pedidos que se entregan a domicilio se les cobran **3.50 € de envío**. La floristería quiere saber cuánto ha facturado por los pedidos a domicilio con el envío incluido.

1. Crea una función lambda llamada `con_envio` que reciba un importe y le sume 3.50 €, redondeando a 2 decimales. **(0,25 puntos)**
2. Con `filter()` y una lambda, obtén los pedidos a domicilio. Muestra solo su código. **(0,5 puntos)**
3. Con `map()` y la lambda `con_envio`, obtén la lista de importes con envío de los pedidos a domicilio. **(0,5 puntos)**
4. Con `reduce()`, calcula el **total** de esos importes con envío. **(0,5 puntos)**
5. Con `reduce()` y una lambda, obtén el **pedido con más ramos** de todos. Muestra el nombre del cliente. **(0,5 puntos)**
6. Con `sorted()` y una lambda, ordena todos los pedidos **de menor a mayor importe**. Muestra solo los códigos. **(0,25 puntos)**

**Salida esperada**

```
['F01', 'F03', 'F05']
[28.5, 42.0, 75.5]
Total a domicilio con envío: 146.0 €
Pedido con más ramos: Elena
['F04', 'F01', 'F03', 'F02', 'F05']
```

---

## Pregunta 2 · Refactorización del programa de una tintorería (2,5 puntos)

Una tintorería tiene un programa que **funciona**, pero está escrito todo seguido: listas con posiciones difíciles de recordar, muchos `if/elif` según el tipo de prenda y cálculos repetidos. Tu tarea es **reorganizarlo usando clases, objetos, herencia y polimorfismo**, sin cambiar lo que muestra por pantalla.

### Parte A. Analizar el código original (sin puntuación)

Copia el código y ejecútalo para ver su salida. **No lo modifiques todavía.**

```python
# Programa original de la tintorería
# Cada encargo: [tipo, cliente, unidades, tarjeta_cliente]
encargos = [
    ["camisa", "Laura Gómez", 3, False],
    ["pantalon", "Sergio Martín", 2, True],
    ["edredon", "Rosa Díaz", 1, False],
    ["camisa", "Javier Soto", 8, True],
    ["edredon", "Pilar Vega", 2, True],
]

total = 0
for e in encargos:
    if e[0] == "camisa":
        precio = e[2] * 2.5
        if precio > 15:
            precio = 15
        if e[3]:
            precio = precio * 0.8
        print("CAMISA | " + e[1] + " | " + str(e[2]) + " uds. | " + str(round(precio, 2)) + " €")
    elif e[0] == "pantalon":
        precio = e[2] * 4.0
        if e[3]:
            precio = precio * 0.8
        print("PANTALON | " + e[1] + " | " + str(e[2]) + " uds. | " + str(round(precio, 2)) + " €")
    elif e[0] == "edredon":
        precio = e[2] * 12.0 + 3
        if e[3]:
            precio = precio * 0.8
        print("EDREDON | " + e[1] + " | " + str(e[2]) + " uds. | " + str(round(precio, 2)) + " €")
    total = total + precio

print("TOTAL TINTORERÍA: " + str(round(total, 2)) + " €")

# Contar encargos de más de 10 €: hay que repetir todos los cálculos
caros = 0
for e in encargos:
    if e[0] == "camisa":
        precio = e[2] * 2.5
        if precio > 15:
            precio = 15
    elif e[0] == "pantalon":
        precio = e[2] * 4.0
    elif e[0] == "edredon":
        precio = e[2] * 12.0 + 3
    if e[3]:
        precio = precio * 0.8
    if precio > 10:
        caros = caros + 1

print("Encargos de más de 10 €: " + str(caros))
```

Las reglas de precio que esconde el código son:

| Tipo de prenda | Cálculo del precio base |
| --- | --- |
| Camisa | unidades × 2.50 €, con un máximo de 15 € por encargo. |
| Pantalón | unidades × 4 €. |
| Edredón | unidades × 12 € + 3 € por la bolsa especial. |
| Todas | Si el cliente tiene la tarjeta de la tienda, se aplica un 20 % de descuento sobre el precio base. |

### Parte B. Crear la superclase (0,75 puntos)

Crea una clase `Encargo` con:

- **Atributos:** `cliente`, `unidades` y `tarjeta` (por defecto `False`).
- **Atributo de clase `DESCUENTO_TARJETA`:** vale 0.8.
- **Método `precio_base()`:** en la superclase devuelve unidades × 1 €.
- **Método `precio_total()`:** aplica el descuento de la tarjeta sobre `precio_base()` cuando corresponda. Se escribe **solo en la superclase**.
- **Método `__str__`:** devuelve la línea completa con el formato del programa original. El tipo (`CAMISA`, `PANTALON`…) se obtiene a partir del nombre de la clase.

### Parte C. Crear las subclases (0,5 puntos)

Crea `EncargoCamisa`, `EncargoPantalon` y `EncargoEdredon`. Cada una debe sobrescribir `precio_base()` **solo si lo necesita**.

Pista para el tipo: si la clase se llama `EncargoCamisa`, puedes obtener `"CAMISA"` con `type(self).__name__.replace("Encargo", "").upper()`.

### Parte D. Crear una clase que agrupe los encargos (composición) (0,5 puntos)

Crea una clase `Tintoreria` que **contenga** una lista de encargos y tenga estos métodos:

- `agregar(encargo)`;
- `mostrar()`, que imprime cada encargo;
- `total()`, que devuelve la suma de los precios totales;
- `contar_superiores_a(importe)`, que devuelve cuántos encargos superan ese importe.

### Parte E. Reescribir el programa principal (0,25 puntos)

```python
tintoreria = Tintoreria()
tintoreria.agregar(EncargoCamisa("Laura Gómez", 3))
tintoreria.agregar(EncargoPantalon("Sergio Martín", 2, True))
tintoreria.agregar(EncargoEdredon("Rosa Díaz", 1))
tintoreria.agregar(EncargoCamisa("Javier Soto", 8, True))
tintoreria.agregar(EncargoEdredon("Pilar Vega", 2, True))

tintoreria.mostrar()
print(f"TOTAL TINTORERÍA: {round(tintoreria.total(), 2)} €")
print(f"Encargos de más de 10 €: {tintoreria.contar_superiores_a(10)}")
```

**Salida esperada** (idéntica a la del programa original)

```
CAMISA | Laura Gómez | 3 uds. | 7.5 €
PANTALON | Sergio Martín | 2 uds. | 6.4 €
EDREDON | Rosa Díaz | 1 uds. | 15.0 €
CAMISA | Javier Soto | 8 uds. | 12.0 €
EDREDON | Pilar Vega | 2 uds. | 21.6 €
TOTAL TINTORERÍA: 62.5 €
Encargos de más de 10 €: 3
```

### Parte F. Ampliación (0,5 puntos)

La tintorería empieza a limpiar **alfombras**. Su precio base es unidades × 18 € + 10 € por la recogida a domicilio. Crea `EncargoAlfombra` y añade este encargo:

```python
tintoreria.agregar(EncargoAlfombra("Andrés Ruiz", 1))
```

**Salida esperada** (solo las líneas nuevas o que cambian)

```
ALFOMBRA | Andrés Ruiz | 1 uds. | 28.0 €
TOTAL TINTORERÍA: 90.5 €
Encargos de más de 10 €: 4
```

### Restricciones

- En el programa final **no puede quedar ningún `if/elif` que pregunte por el tipo de prenda**.
- No se puede usar `isinstance()` para decidir cómo calcular el precio.
- El cálculo de cada tipo de prenda y el descuento de la tarjeta deben estar escritos **en un único sitio**.
- Para añadir las alfombras **no debes modificar** ni `Encargo` ni `Tintoreria`.

---

## Pregunta 3 · Alquiler de bicicletas (2,5 puntos)

Una empresa de alquiler de bicicletas quiere un pequeño programa para analizar los alquileres del día. Esta pregunta combina clases, herencia, polimorfismo, comprehensions, programación funcional y recursión.

### Parte A. Jerarquía de clases (0,5 puntos)

1. Crea una superclase `Bicicleta` con `modelo` y `precio_hora`, un método `precio_final()` que devuelva el precio por hora y un método `__str__` con el formato `Paseo Classic - 5.00 €/h`, usando `precio_final()`.
2. Crea estas subclases:
    - `BiciElectrica`: tiene un recargo fijo de 4 € por hora por el uso de la batería;
    - `BiciInfantil`: tiene un 20 % de descuento sobre su precio por hora (redondea a 2 decimales).

### Parte B. Datos del día (sin puntuación)

```python
alquileres = [
    {"cliente": "Irene",  "bici": BiciElectrica("Urban E-200", 8.0),  "horas": 3},
    {"cliente": "Tomás",  "bici": Bicicleta("Paseo Classic", 5.0),    "horas": 2},
    {"cliente": "Irene",  "bici": BiciInfantil("Mini Rider", 4.0),    "horas": 2},
    {"cliente": "Marcos", "bici": Bicicleta("Montaña Pro", 7.5),      "horas": 4},
    {"cliente": "Nuria",  "bici": BiciElectrica("Cargo E-500", 10.0), "horas": 1},
]
```

### Parte C. Comprehensions (0,75 puntos)

1. Una **lista** con el importe de cada alquiler (`precio_final() × horas`), redondeado a 2 decimales.
2. Un **set** con los clientes distintos, ordenado alfabéticamente al mostrarlo.
3. Un **diccionario** `modelo de bici → precio final por hora` de todas las bicis.

### Parte D. Programación funcional (0,5 puntos)

1. Con `filter()`, obtén los alquileres de **bicis eléctricas**. Muestra el modelo. Pista: `isinstance()`.
2. Con `map()` y `reduce()`, calcula la **facturación total** del día.

### Parte E. Recursión (0,25 puntos)

Escribe una función recursiva `contar_horas(alquileres)` que devuelva el total de horas alquiladas, **sin usar bucles**.

### Parte F. Informe final (0,5 puntos)

Muestra un informe con este aspecto:

```
=== FLOTA DEL DÍA ===
Urban E-200 - 12.00 €/h
Paseo Classic - 5.00 €/h
Mini Rider - 3.20 €/h
Montaña Pro - 7.50 €/h
Cargo E-500 - 14.00 €/h

Importes por alquiler: [36.0, 10.0, 6.4, 30.0, 14.0]
Clientes distintos: ['Irene', 'Marcos', 'Nuria', 'Tomás']
Precios por hora: {'Urban E-200': 12.0, 'Paseo Classic': 5.0, 'Mini Rider': 3.2, 'Montaña Pro': 7.5, 'Cargo E-500': 14.0}
Bicis eléctricas alquiladas: ['Urban E-200', 'Cargo E-500']
Facturación total: 96.4 €
Horas alquiladas: 12
```

---

## Pregunta 4 · Del notebook a un proyecto modular (2,5 puntos)

### Contexto

<aside>

**Cafeterías Aroma** es una cadena con tres locales: *Centro*, *Puerto* y *Estación*. Una analista de ventas ha preparado en un notebook el **informe de ventas por local**:

1. Lee los tickets del día, que llegan en formato CSV.
2. Descarta los tickets con las unidades o el precio vacíos o mal escritos.
3. Descarta los tickets devueltos.
4. Calcula el importe de cada ticket: unidades × precio, con un **5 % de descuento si se compran 4 unidades o más**, y después se suma el **10 % de IVA**.
5. Suma unidades e importes por local, ordena de mayor a menor importe y calcula el **importe medio por unidad**.
6. Muestra el informe por pantalla y lo guarda en `informe_ventas.csv`.

La dirección quiere que el informe se ejecute **automáticamente cada noche**. El trabajo consiste en convertir el notebook en un proyecto Python modular que haga **exactamente lo mismo**.

</aside>

### El notebook `informe_ventas.ipynb`

Crea el notebook en VS Code o Jupyter con las siguientes celdas y ejecútalo para comprobar la salida antes de empezar a modularizar.

**Celda [1]** · Cargar los datos

```python
datos = """ticket,local,producto,unidades,precio,estado
T01,centro,Café con leche,3,1.80,pagado
T02,PUERTO, tostada ,2,2.50,pagado
T03,Centro,zumo natural,x,3.00,pagado
T04,estación,café con leche,5,1.80,DEVUELTO
T05,Estación,croissant,4,1.60,pagado
T06,puerto,café con leche,2,1.80,pagado
T07,Centro,tostada,1,2.50,pagado
T08,estación,zumo natural,2,3.00,pagado"""
lineas = datos.split("\n")[1:]
print("Tickets leídos:", len(lineas))
```

```
Tickets leídos: 8
```

**Celda [2]** · Limpiar y descartar errores

```python
ventas = []
errores = []
for l in lineas:
    c = [x.strip() for x in l.split(",")]
    try:
        u = int(c[3])
        p = float(c[4])
        ventas.append([c[0], c[1].title(), c[2].lower(), u, p, c[5].lower()])
    except ValueError:
        errores.append(c[0])
print("Tickets con errores:", errores)
```

```
Tickets con errores: ['T03']
```

**Celda [3]** · Quitar los tickets devueltos

```python
devueltos = [v[0] for v in ventas if v[5] == "devuelto"]
ventas = [v for v in ventas if v[5] != "devuelto"]
print("Tickets devueltos:", devueltos)
print("Tickets válidos:", len(ventas))
```

```
Tickets devueltos: ['T04']
Tickets válidos: 6
```

**Celda [4]** · Calcular el importe de cada ticket

```python
def tiene_descuento(v):
    return v[3] >= 4

for v in ventas:
    base = v[3] * v[4]
    if tiene_descuento(v):
        base = base * 0.95
    v.append(round(base * 1.10, 2))
print(ventas[0])
```

```
['T01', 'Centro', 'café con leche', 3, 1.8, 'pagado', 5.94]
```

**Celda [5]** · Agregar por local

```python
ingresos = {}
unidades = {}
for v in ventas:
    ingresos[v[1]] = round(ingresos.get(v[1], 0) + v[6], 2)
    unidades[v[1]] = unidades.get(v[1], 0) + v[3]
ingresos = dict(sorted(ingresos.items(), key=lambda x: x[1], reverse=True))
```

**Celda [6]** · Mostrar el informe

```python
print("Informe de ventas por local:")
for h, t in ingresos.items():
    print(f"  {h:<10}{unidades[h]:>3} uds. {t:>8.2f} €   media/ud. {t/unidades[h]:>6.2f} €")
print(f"  {'TOTAL':<10}{sum(unidades.values()):>3} uds. {sum(ingresos.values()):>8.2f} €")
```

```
Informe de ventas por local:
  Estación    6 uds.    13.29 €   media/ud.   2.21 €
  Puerto      4 uds.     9.46 €   media/ud.   2.37 €
  Centro      4 uds.     8.69 €   media/ud.   2.17 €
  TOTAL      14 uds.    31.44 €
```

**Celda [7]** · Guardar el informe en CSV

```python
with open("informe_ventas.csv", "w", encoding="utf-8") as f:
    f.write("local,unidades,ingresos\n")
    for h, t in ingresos.items():
        f.write(f"{h},{unidades[h]},{t}\n")
print("Informe guardado en informe_ventas.csv")
```

```
Informe guardado en informe_ventas.csv
```

Contenido de `informe_ventas.csv`:

```
local,unidades,ingresos
Estación,6,13.29
Puerto,4,9.46
Centro,4,8.69
```

### Parte A · El proyecto modular (1,5 puntos)

**Estructura mínima exigida**

```
cafeterias_etl/
├── main.py                 ← punto de entrada
└── etl/                    ← paquete del pipeline
    ├── __init__.py         ← recepción del paquete
    ├── config.py           ← reglas de negocio y parámetros
    ├── modelos.py          ← clase Venta
    ├── transformacion.py   ← leer, parsear, validar, convertir y filtrar
    └── carga.py            ← clase InformeVentas + exportar a CSV
```

**Requisitos por módulo**

| Módulo | Requisitos |
| --- | --- |
| `config.py` | Solo constantes en mayúsculas: descuento por volumen, unidades mínimas para el descuento, IVA, estado de devolución, número de campos de cada línea y nombre del fichero de salida. Ningún otro módulo puede tener esos valores escritos «a mano» |
| `modelos.py` | Clase `Venta` con atributos con nombre (`id_ticket`, `local`, `producto`, `unidades`, `precio`, `estado`). Una `@property` `tiene_descuento` y una `@property` `importe_total` que **se calcula** al pedirla (no se guarda como columna). |
| `transformacion.py` | Funciones **puras**: `leer_lineas(texto)` (devuelve las líneas sin la cabecera), `parsear(linea)`, `es_valida(campos)`, `a_venta(campos)` y `transformar(lineas)`. `es_valida()` debe comprobar también que la línea tiene exactamente 6 campos. `transformar()` devuelve las ventas activas, los ids con errores y los ids devueltos. Usa al menos una comprehension |
| `carga.py` | Clase `InformeVentas` con `cargar(ventas)`, `por_local()` (devuelve, ordenado de mayor a menor importe, un diccionario `{local: (unidades, ingresos)}`) y `total()`. Función `exportar_csv(informe, ruta)` que genera el CSV |
| `__init__.py` | Expone `leer_lineas`, `transformar`, `InformeVentas`, `exportar_csv` y la constante con el nombre del fichero de salida. Define `__all__` |
| `main.py` | Contiene los datos de entrada, una función `mostrar_informe(informe)`, una función `main()` que llama a las piezas del paquete en el orden correcto y el bloque `if __name__ == "__main__":`. **Solo importa del paquete `etl`**, nunca de sus módulos internos |

**Reglas de importación**

- Dentro del paquete `etl` se usan **imports relativos** (`from .config import IVA`).
- Desde `main.py` se usan **imports absolutos** a través de la recepción (`from etl import leer_lineas, transformar, InformeVentas, exportar_csv`).
- No puede haber **imports circulares**: el sentido de las dependencias es `config` → `modelos` → `transformacion` / `carga` → `__init__` → `main`.

### Parte B · Ejecución y comprobación (0,5 puntos)

Desde la carpeta del proyecto:

```powershell
cd cafeterias_etl
python main.py
```

**Salida esperada** (debe ser **idéntica** a la del notebook, sin la fila de la celda 4):

```
Tickets leídos: 8
Tickets con errores: ['T03']
Tickets devueltos: ['T04']
Tickets válidos: 6
Informe de ventas por local:
  Estación    6 uds.    13.29 €   media/ud.   2.21 €
  Puerto      4 uds.     9.46 €   media/ud.   2.37 €
  Centro      4 uds.     8.69 €   media/ud.   2.17 €
  TOTAL      14 uds.    31.44 €
Informe guardado en informe_ventas.csv
```

El fichero `informe_ventas.csv` generado debe tener **el mismo contenido** que el del notebook.

### Parte C · Probar piezas por separado (0,5 puntos)

Crea un archivo `pruebas_manuales.py` en la carpeta `cafeterias_etl` que importe **solo** las funciones de `etl.transformacion` y compruebe estos casos sin ejecutar el pipeline completo:

```python
from etl.transformacion import parsear, es_valida, a_venta

print(es_valida(parsear("T10,Centro,tostada,2,2.50,pagado")))
print(es_valida(parsear("T11,Centro,bocadillo,3,4,20,pagado")))
print(es_valida(parsear("T12,Centro,zumo natural,,3.00,pagado")))
print(a_venta(parsear("T13, Puerto ,TOSTADA,4,2.50,Pagado")).importe_total)
```

**Salida esperada:**

```
True
False
False
10.45
```

---


## Pregunta 5 · Mini aplicación con paquetes y subpaquetes (2,5 puntos)

Diseña y programa una **mini aplicación de temática libre** cuyo código esté organizado en **paquetes y subpaquetes** y que se ejecute desde un único `main.py`.

### Requisito estructural mínimo

- **2 paquetes** de primer nivel.
- **1 subpaquete** dentro de cada paquete.
- **2 módulos con código** en cada subpaquete.

```
mi_aplicacion/
├── main.py
├── paquete_1/
│   ├── __init__.py
│   └── subpaquete_1/
│       ├── __init__.py
│       ├── modulo_a.py
│       └── modulo_b.py
└── paquete_2/
    ├── __init__.py
    └── subpaquete_2/
        ├── __init__.py
        ├── modulo_c.py
        └── modulo_d.py
```
