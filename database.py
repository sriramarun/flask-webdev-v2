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

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"), {"val": id})
    row = result.all()
    if len(row) == 0:
      return None
    else:
      return dict(row[0]._mapping)
    
def add_application_to_db(job_id, application):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

          # Create a dictionary of parameters
    params = {
        'job_id': job_id,
        'full_name': application['full_name'],
        'email': application['email'],
        'linkedin_url': application['linkedin_url'],
        'education': application['education'],
        'work_experience': application['work_experience'],
        'resume_url': application['resume_url']
    }

    # Execute with parameters as a dictionary
    conn.execute(query, params)
    conn.commit()