import langchain
from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain.chains import sql_database
from langchain_experimental.sql import SQLDatabaseChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _postgres_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
import os
from few_shots import few_shots

from dotenv import load_dotenv

load_dotenv()

def get_few_shot_db_chain():
	llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)
	db_user = 'postgres'
	db_password = 'postgres123'
	db_host = 'localhost'
	db_name = 'sales_db'
	db = SQLDatabase.from_uri(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:5433/{db_name}", sample_rows_in_table_info=3)
	
	HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
	to_vectorize = [' '.join(shot.values()) for shot in few_shots]
	vectorstore = Chroma.from_texts(to_vectorize, embedding=embeddings, metadatas=few_shots)

	sample_select = SemanticSimilarityExampleSelector(vectorstore=vectorstore, k=2)

	sample_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult", "Answer",],
    template="\nQuestion:{Question}\nSQLQuery:{SQLQuery}\nSQLResult:{SQLResult}\nAnswer:{Answer}",
)

	FewShotPromptTemplate(
	example_select = sample_select,
	example_prompt = sample_prompt,
	prefix = _postgres_prompt,
	suffix = PROMPT_SUFFIX,
	input_variables = ["input", "table_info", "top_k"],
	)
	new_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)

if __name__ == '__main__':
	chain = get_few_shot_db_chain()


