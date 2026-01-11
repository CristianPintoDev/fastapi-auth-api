# FastAPI Backend Learning 🚀

Proyecto para aprender, poner en practica y recordar como construir un backend con **FastAPI**, aplicando buenas prácticas de arquitectura, autenticación y seguridad.

---
## 🔗 **API en producción (Render):**  
  👉 https://fastapi-backend-learning.onrender.com/docs

## 🎯 Objetivo del proyecto

El objetivo de este proyecto es servir como **base sólida de aprendizaje** para:

* Construcción de APIs REST con FastAPI
* Separación por capas (router, service, schema, model)
* Autenticación con JWT (login y protección de rutas)
* Manejo seguro de contraseñas con `passlib` y `bcrypt`
* Uso de dependencias (`Depends`) para seguridad
* Configuración con `pydantic-settings`

Este proyecto **no busca ser un sistema final**, sino una **base profesional y reutilizable**.

---

## 🧱 Estructura del proyecto

```
app/
├── main.py
├── core/
│   ├── config.py        # Settings y variables de entorno
│   ├── database.py      # Conexión a la base de datos
│   └── security.py      # Hash de contraseñas y JWT
├── users/
│   ├── model.py
│   ├── schema.py
│   ├── service.py
│   └── router.py
├── auth/
│   ├── schema.py
│   ├── service.py
│   ├── router.py
|   └── dependencies.py
...

---

## 🔐 Autenticación

* Login mediante `/auth/login`
* Generación de **JWT Bearer Token**
* Protección de endpoints usando:

```python
current_user = Depends(get_current_user)
```

El token se envía **exclusivamente por header**:

```
Authorization: Bearer <token>
```

Totalmente compatible con Swagger UI.

---

## 🧪 Uso en Swagger

1. Ejecutar el proyecto
2. Ir a `/docs`
3. Hacer login en `/auth/login`
4. Copiar el `access_token`
5. Presionar **Authorize**
6. Escribir:

```
Bearer <access_token>
```

7. Probar endpoints protegidos

---

## 🛠️ Tecnologías usadas

* Python 3.10+
* FastAPI
* SQLAlchemy
* Pydantic v2
* passlib + bcrypt
* JWT (python-jose)
* Uvicorn

---

## ✅ Estado del proyecto

✔ Arquitectura limpia
✔ Autenticación funcional
✔ Errores críticos resueltos
✔ Buenas prácticas aplicadas

📌 Proyecto **finalizado como base de aprendizaje**.

---

## 📄 Licencia

Proyecto con fines educativos.
Libre de usar, modificar y extender.

---

✍️ Autor: Cristian Pinto
