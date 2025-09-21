from dotenv import load_dotenv
import os
from supabase import create_client, Client


load_dotenv()

url = os.environ.get("SUPABASE_URL")
key  = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def save_message_to_db(text: str):
    supabase.table("info").insert({"messages": text}).execute()
    # data = supabase.table("info").select("messages").execute()

def get_recent_messages(limit = 25):
    res = supabase.table("info").select('messages').order("created_at", desc=True).limit(limit).execute()
    rows = res.data or []
    texts = [r.get("messages", "") for r in rows if r.get("messages")]
    return "\n\n".join(texts)


