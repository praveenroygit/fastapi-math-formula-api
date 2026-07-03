from database import get_connection

try:
    conn = get_connection()
    print("✅ Connected to MySQL successfully!")

    conn.close()
    print("✅ Connection closed.")

except Exception as e:
    print("❌ Error:", e)