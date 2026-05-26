# Proyecto Final: Análisis de Datos en AquaLimpia S.A.

Este repositorio lo armé para subir el desarrollo del caso práctico de AquaLimpia S.A. La empresa estaba teniendo problemas intermitentes con la calidad del agua tratada (específicamente con los niveles de DBO de salida) y no lograban identificar un patrón claro. 

Mi objetivo con este proyecto fue agarrar los datos operativos de las plantas, ordenarlos a través de Python, armar unos gráficos descriptivos y automatizar la entrega de reportes específicos para las áreas que los necesitan (Operaciones y Gestión Ambiental).

---

## Organización de los archivos

Para que el código no fuera un desorden, separé las cosas siguiendo las buenas prácticas de modularidad:

* **`main.ipynb`**: Es el Jupyter Notebook principal. Acá hago la carga de datos, muestro las estadísticas, el gráfico de cajas (Boxplot) y coordino todo el flujo.
* **`utils.py`**: Este script externo es donde dejé guardadas las funciones de backend (`evaluar_calidad_datos`, `generar_reporte_operaciones` y `generar_reporte_ambiental`). Así el notebook queda limpio y las funciones se pueden reutilizar cuando entren datos nuevos.
* **`dataset_set_A_aguas_residuales.xlsx`**: El archivo Excel original con el histórico de las plantas.
* **`reporte_operaciones.csv`**: El Excel que genera mi script de forma automática con las variables del día a día técnico (caudal, lodos, energía, DBO).
* **`reporte_ambiental.csv`**: La otra salida automática, pero enfocada en lo legal, que calcula directo si la planta cumple o no con la norma.

---

## Requisitos para correr el proyecto

Si quieres clonar esto y probarlo de forma local, necesitas tener Python 3 y estas librerías instaladas:

```bash
pip install pandas matplotlib seaborn openpyxl
