import timeit
import pprint

from SPARQLWrapper import SPARQLWrapper, JSON

from query_data import data_experimental, data_experimental_getty


#return value latency in a list
def get_value_latency():

	iterador = 2

	times = []
	for i in range(iterador):
		start_latency = timeit.default_timer()
		json_response = execute_query(
			data_experimental['url'], data_experimental['queries'][0]
			)
		final_latency = timeit.default_timer()
		time_latency = final_latency - start_latency
		times.append(time_latency)

	return times



#return a comment text clean
def clean_syntactic_validity():
	json_response = execute_query(
			data_experimental_getty['url'],
			data_experimental_getty['queries'][0]
			)
	return json_response



#return value timeliness
def get_value_timeliness():
	json_response = execute_query(
		data_experimental['url'], data_experimental['queries'][0]
		)

	return json_response


#return value timeliness
def get_value_scalability():
	json_response = execute_query(
		data_experimental['url'], data_experimental['queries'][0]
		)
	return json_response

#return a dict
def execute_query(endpoint, query):
	sparql = SPARQLWrapper(endpoint)
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	pprint.pprint(results, width=1)

	return results



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