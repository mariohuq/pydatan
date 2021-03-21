def process2(conn):
    conn.send([42, None, 'hello'])
    x = conn.recv()
    print(f'process2: x={x}')
    conn.close()