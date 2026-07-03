from database import get_connection




def save_calculation(operation, a, b, result):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO calculations
    (operation, a, b, result)
    VALUES (%s, %s, %s, %s)
    """

    values = (operation, a, b, result)

    cursor.execute(query, values)

    conn.commit()

    cursor.close()

    conn.close()


def get_all_calculations():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM calculations
    ORDER BY id DESC
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()

    conn.close()

    return rows
def get_calculation_by_id(calculation_id):

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM calculations
    WHERE id = %s
    """

    cursor.execute(query, (calculation_id,))

    row = cursor.fetchone()

    cursor.close()

    conn.close()

    return row


def update_calculation_by_id(calculation_id, operation, a, b, result):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE calculations
    SET operation = %s,
        a = %s,
        b = %s,
        result = %s
    WHERE id = %s
    """

    values = (operation, a, b, result, calculation_id)

    cursor.execute(query, values)
    conn.commit()

    updated_rows = cursor.rowcount

    cursor.close()
    conn.close()

    return updated_rows
def delete_calculation_by_id(calculation_id):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM calculations
    WHERE id = %s
    """

    cursor.execute(query, (calculation_id,))
    conn.commit()

    deleted_rows = cursor.rowcount

    cursor.close()
    conn.close()

    return deleted_rows

