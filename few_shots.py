few_shots = [
{
	"Question": "How many eden tea do we have left for 50g?",
	'SQLQuery': "SELECT sum(stock_quantity) FROM fmcg_retail_goods where item='Eden Tea 50g' ",
	'SQLResult': "Result of the SQL query",
	'Answer': 'qns1' },
	{
	"Question": "How much is the total price of the inventory for all 2kgs Ngano flour?",
	'SQLQuery': "SELECT sum(price * stock_quantity) FROM fmcg_retail_goods where item='Ngano Flour 2kgs'",
	'SQLResult': "Result of the SQL query",
	'Answer': 'qns2' },
{
	"Question": "If we have to sell all the tissue in the store today, how much revenue will be generated?",
	'SQLQuery': "SELECT sum(price * stock_quantity) FROM fmcg_retail_goods where item='Tissue'",
	'SQLResult': "Result of the SQL query",
	'Answer': 'qns3' },

	{
	"Question": "If we have to sell all the items in our inventory how much revenue will be generated?",
	'SQLQuery': "SELECT sum(price * stock_quantity) FROM fmcg_retail_goods ",
	'SQLResult': "Result of the SQL query",
	'Answer': 'qns4' },

	{
	"Question": "how many ordinary biro pen do we have left in stock?",
	'SQLQuery': "SELECT sum(stock_quantity) FROM fmcg_retail_goods where item='Ordinary Biro Pen'",
	'SQLResult': "Result of the SQL query",
	'Answer': 'qns5' },

	{
	"Question": "What is the running total of each item type in the inventory?",
	'SQLQuery': "SELECT id, item, sum(price*stock_quantity) OVER (PARTITION BY item order by 3) AS running_total from fmcg_retail_goods",
	'SQLResult': "Result of the SQL query",
	'Answer': 'qns6' }
]