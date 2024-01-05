few_shots = [
{
	"Question": "How many t-shirts do we have left for Nike in XS size and white color?",
	'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts where brand='Nike' AND color='white' ",
	'SQLResult': "Result of the SQL query",
	'Answer': qns1 },
	{
	"Question": "How much is the total price of the inventory for all S-size t-shirts?",
	'SQLQuery': "SELECT sum(price * stock_quantity) FROM t_shirts where size='S'",
	'SQLResult': "Result of the SQL query",
	'Answer': qns2 },
{
	"Question": "If we have to sell all the Levi's t-shirts today with disounts applied, how much revenue will be generated?",
	'SQLQuery': "SELECT sum(price * stock_quantity) FROM t_shirts where size='S'",
	'SQLResult': "Result of the SQL query",
	'Answer': qns3 },

	{
	"Question": "If we have to sell all the Levi's t-shirts today, how much revenue will be generated?",
	'SQLQuery': "SELECT sum(price * stock_quantity) FROM t_shirts where brand='Levi'",
	'SQLResult': "Result of the SQL query",
	'Answer': qns4 },

	{
	"Question": "how many white color Levi's shirts are there?",
	'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts where brand='Levi' AND color='white'",
	'SQLResult': "Result of the SQL query",
	'Answer': qns5 }
]