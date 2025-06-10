import argparse
import sqlite3
import datetime

DB_NAME = 'services.db'

SERVICES = {
    'tyre_change': 'Переобувка',
    'balancing': 'Балансировка',
    'wheel_repair': 'Ремонт колеса'
}

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS records ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'plate TEXT NOT NULL,'
        'service TEXT NOT NULL,'
        'timestamp TEXT NOT NULL'
        ')'
    )
    conn.commit()
    conn.close()


def add_record(plate: str, service: str):
    if service not in SERVICES:
        raise ValueError(f"Unknown service: {service}")
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO records (plate, service, timestamp) VALUES (?, ?, ?)',
        (plate.upper(), service, datetime.datetime.now().isoformat())
    )
    conn.commit()
    conn.close()


def list_records():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('SELECT plate, service, timestamp FROM records ORDER BY id')
    rows = cur.fetchall()
    conn.close()
    return rows


def main():
    parser = argparse.ArgumentParser(description='Service Records App')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a service record')
    add_parser.add_argument('plate', help='License plate number')
    add_parser.add_argument('service', choices=SERVICES.keys(), help='Service type')

    subparsers.add_parser('list', help='List all records')

    args = parser.parse_args()

    init_db()

    if args.command == 'add':
        add_record(args.plate, args.service)
        print('Record added.')
    elif args.command == 'list':
        for plate, service, ts in list_records():
            print(f"{ts} | {plate} | {SERVICES.get(service, service)}")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
