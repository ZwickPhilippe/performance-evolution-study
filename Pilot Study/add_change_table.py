import sqlite3

# connect to database
conn = sqlite3.connect('database/infer_results.db')

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS CHANGE(project_id integer, release_prior integer, 
hash text, procedure_id text, reason text,change_level integer, increase boolean, difference text, FOREIGN KEY(project_id) REFERENCES PROJECT(id),
FOREIGN KEY(release_prior) REFERENCES RELEASE(id), FOREIGN KEY(hash) REFERENCES FUNCTION(HASH), PRIMARY KEY (hash, procedure_id, release_prior, project_id))
""")

conn.commit()

