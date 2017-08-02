import pprint

from SPARQLWrapper import SPARQLWrapper, JSON


def test():
	return 'hello'

#return a dict
def execute_query(endpoint, query):
	sparql = SPARQLWrapper(endpoint)
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	pprint.pprint(results, width=1)

	return results

#return a comment text clean
def clean_syntactic_validity():

	#DO FOR syntanctic_validity

	comments = []
	comments = execute_query()
	comments.append(execute_query())

	pass


def execute_query_example():
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	sparql.setQuery("""
	    PREFIX  dc: <http://purl.org/dc/elements/1.1/>
	PREFIX dct: <http://purl.org/dc/terms/>
	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

	SELECT DISTINCT ?title ?comment 
	where {
	       ?s dct:title ?title .
	       ?s rdfs:comment ?comment .
	     FILTER (lang(?title) = 'en')
	     FILTER (lang(?comment) = 'en')
	} LIMIT 1000
	""")
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()

	pprint.pprint(results, width=1)

	#TODO: DELETE /n in comment
	#query for get comment with /n 
	#results["results"]["bindings"][0]["comment"]["value"]
	for result in results["results"]["bindings"]:
	    print(result["label"]["value"])