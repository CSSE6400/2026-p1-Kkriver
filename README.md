# Week 1 - Basic Flask API

## Overview

This week focuses on building a basic Flask application with a health check endpoint.

---

## Features

- Flask application setup  
- Health check endpoint  

---

## How to Run

### 1. Install dependencies

```bash
poetry install --no-root

## 2. Run the application

```bash
poetry run flask --app todo run -p 6400 --debug

## 3. Test the API

```bash
curl http://127.0.0.1:6400/api/v1/health

## API

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | /api/v1/health | Health check |


