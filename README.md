# Service Records

This repository contains a simple command-line application for recording services performed on vehicles.
Each record stores the license plate number, the type of service, and the time the service was provided.

## Supported services

- `tyre_change` - \u041F\u0435\u0440\u0435\u043e\u0431\u0443\u0432\u043a\u0430
- `balancing` - \u0411\u0430\u043b\u0430\u043d\u0441\u0438\u0440\u043e\u0432\u043a\u0430
- `wheel_repair` - \u0420\u0435\u043c\u043e\u043d\u0442 \u043a\u043e\u043b\u0435\u0441\u0430

## Usage

Add a record:

```bash
python app.py add <LICENSE_PLATE> <SERVICE>
```

Example:

```bash
python app.py add A123BC tyre_change
```

List all records:

```bash
python app.py list
```

The application stores data in `services.db` in the repository directory.
