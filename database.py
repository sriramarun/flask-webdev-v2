from sqlalchemy import create_engine, text
import os
import dotenv

# import dotenv
dotenv.load_dotenv()
# Create the engine with the database URL from the environment variable
engine = create_engine(os.getenv('DATABASE_URL'))

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs



