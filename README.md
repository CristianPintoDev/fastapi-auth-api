# FastAPI Auth API 🚀

REST API built with FastAPI featuring JWT authentication, user management and clean architecture.

---

## 🔗 Live Demo

👉 https://fastapi-auth-api.onrender.com/docs

---

## 🚀 Features

* JWT authentication (login + protected routes)
* User management (CRUD)
* Password hashing with bcrypt
* Layered architecture (router, service, schema, model)
* Dependency-based security with FastAPI

---

## 🧱 Project Structure

```id="r3q9zp"
app/
├── main.py
├── core/
│   ├── config.py
│   ├── database.py
│   └── security.py
├── users/
│   ├── model.py
│   ├── schema.py
│   ├── service.py
│   └── router.py
├── auth/
│   ├── schema.py
│   ├── service.py
│   ├── router.py
│   └── dependencies.py
```

---

## 🔐 Authentication

* Login: `/auth/login`
* Token: JWT Bearer
* Protected endpoints require:

```id="j1zqop"
Authorization: Bearer <token>
```

---

## 🧪 Local Development

```bash id="qf1x5p"
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open in your browser:

```id="4ttd6x"
http://127.0.0.1:8000/docs
```

---

## 🛠️ Tech Stack

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* Passlib (bcrypt)
* JWT (python-jose)

---

## 📌 Status

Core backend functionality implemented:

* Authentication ✔
* User management ✔
* Clean architecture ✔

---

## 👨‍💻 Author

Cristian Pinto


## License

This project is licensed under the MIT License.