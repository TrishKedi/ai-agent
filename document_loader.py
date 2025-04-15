import json
from langchain.docstore.document import Document

NOTES_PATH = "memory/notes.json"
def load_documents(file_path=NOTES_PATH):

    with open(file_path, 'r') as f:
        notes = json.load(f)

        documents = [ Document(
            page_content=note['content'],
            metadata={"title": note['title']}
            ) 
            for note in notes
        ]

        return documents