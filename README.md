# 📚 Gestión de Alumnos / Student Management

> Aplicación de consola en Python para gestionar una lista de alumnos, con menú bilingüe (Español / Inglés). Proyecto realizado como ejercicio de lógica de programación.
>
> Console-based Python application to manage a list of students, with a bilingual menu (Spanish / English). Built as a programming-logic practice project.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

## Tabla de contenidos / Table of contents
- [Español](#-español)
- [English](#-english)
- [Tecnologías / Tech Stack](#️-tecnologías--tech-stack)
- [Licencia / License](#-licencia--license)

---

## 🇪🇸 Español

### 📖 Descripción
Sistema de gestión de alumnos que corre en la terminal. Al iniciar, permite elegir el idioma (Español o Inglés) y luego despliega un menú con operaciones típicas de un CRUD (crear, leer, actualizar y eliminar) sobre una lista de alumnos guardada en memoria.

### ✨ Características
- Selección de idioma al inicio (Español / Inglés)
- Crear un nuevo alumno
- Modificar nombre, apellido o año de nacimiento de un alumno existente
- Eliminar un alumno por ID
- Listar todos los alumnos
- Buscar alumnos por nombre, apellido o una letra
- Buscar un alumno por ID
- Filtrar alumnos por rango de año de nacimiento
- Validación básica de entradas (evita texto donde se esperan números)

### 🗂️ Estructura de datos
Cada alumno se representa como un diccionario:
```python
{
    "id": 1,
    "nombre": "ana",
    "apellido": "garcía",
    "año_nacimiento": 1995,
    "edad": 31
}
```
La lista completa de alumnos se guarda en memoria (`lista_usuarios`) mientras el programa está en ejecución.

### 🧭 Menú principal
```
1- CREAR ALUMNO
2- MODIFICAR ALUMNO
3- ELIMINAR ALUMNO
4- LISTAR ALUMNOS
5- BUSCAR POR APELLIDO, NOMBRE O LETRA
6- ABRIR MENU
7- BUSCAR POR ID
8- FILTRAR POR AÑO DE NACIMIENTO
9- SALIR
```

### ▶️ Cómo ejecutar
Requisitos: Python 3.6 o superior (no requiere librerías externas).

```bash
python3 gestion_alumnos.py
```
> Reemplazá `gestion_alumnos.py` por el nombre real del archivo si lo guardaste con otro nombre.

### 📌 Notas
- Los datos se almacenan solo en memoria: al cerrar el programa se pierden los cambios (no hay persistencia en archivo ni base de datos).
- El proyecto fue pensado principalmente como práctica de lógica (bucles, condicionales, funciones, manejo de listas y diccionarios), no como una aplicación de producción.

### 🚀 Posibles mejoras
- Persistir los datos en un archivo (JSON, CSV o base de datos)
- Agregar manejo de excepciones más robusto
- Separar la lógica en módulos (uno por idioma o por funcionalidad)
- Sumar tests automatizados

---

## 🇬🇧 English

### 📖 Description
Console-based student management system. On startup, it lets you choose the interface language (Spanish or English) and then shows a menu with typical CRUD operations (create, read, update, delete) over a list of students kept in memory.

### ✨ Features
- Language selection on startup (Spanish / English)
- Create a new student
- Modify a student's name, last name, or birth year
- Delete a student by ID
- List all students
- Search students by name, last name, or a single letter
- Search a student by ID
- Filter students by birth year range
- Basic input validation (prevents text where numbers are expected)

### 🗂️ Data structure
Each student is represented as a dictionary:
```python
{
    "id": 1,
    "nombre": "ana",
    "apellido": "garcía",
    "año_nacimiento": 1995,
    "edad": 31
}
```
The full list of students (`database_records`) is kept in memory while the program runs.

### 🧭 Main menu
```
1- CREATE STUDENT
2- MODIFY STUDENT
3- DELETE STUDENT
4- LIST STUDENTS
5- SEARCH BY LAST NAME, NAME OR LETTER
6- OPEN MENU
7- SEARCH BY ID
8- FILTER BY BIRTH YEAR
9- EXIT
```

### ▶️ How to run
Requirements: Python 3.6+ (no external libraries needed).

```bash
python3 gestion_alumnos.py
```
> Replace `gestion_alumnos.py` with the actual filename if you saved it under a different name.

### 📌 Notes
- Data is stored in memory only: closing the program discards all changes (no file or database persistence).
- This project was built mainly as logic practice (loops, conditionals, functions, and working with lists/dictionaries), not as a production-ready application.

### 🚀 Possible improvements
- Persist data to a file (JSON, CSV, or a database)
- Add more robust exception handling
- Split the logic into modules (per language or per feature)
- Add automated tests

---

## 🛠️ Tecnologías / Tech Stack
- Python 3 (uso exclusivo de librerías estándar / standard library only)

## 👤 Autor / Author
- Jeremias / Your name here — [GitHub](https://github.com/jeremias1234-bit/)

