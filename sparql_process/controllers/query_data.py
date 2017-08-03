DATAHUB_ENDPOINT = 'http://dbpedia.org/sparql'
GETTY_ENDPOINT = 'http://vocab.getty.edu/sparql'
VIRTUOSO_ENDPOINT = 'http://linkeddata.ge.imati.cnr.it:8890/sparql'
OPENDATA_CZ = 'http://linked.opendata.cz/sparql'

#works with 2 items virtuoso
data_experimental = {
				'url': OPENDATA_CZ,
				'criteria': ['timeliness', 'latency', 'scalability'],
				'queries': [
					"""
						PREFIX  dc: <http://purl.org/dc/elements/1.1/>
						PREFIX dct: <http://purl.org/dc/terms/>

						SELECT DISTINCT ?title ?created ?issued
						where {
						    ?s dct:title ?title .
						    ?s dct:created ?created .
						    ?s dct:issued ?issued .
						} LIMIT 1000
					"""]
			}

#not works in remote get
data_experimental_getty = {
				'url': GETTY_ENDPOINT,
				'criteria': ['syntactic_validity'],
				'queries': [
					"""
						PREFIX  dc: <http://purl.org/dc/elements/1.1/>
						PREFIX dct: <http://purl.org/dc/terms/>

						SELECT DISTINCT ?title ?description
						where {
						   ?s dct:title ?title .
						 ?s dct:description ?description .
						} LIMIT 1000
					"""]
			}


data = {
	'syntactic_validity': {
		'test_data': {
			'datahub': {
				'url': DATAHUB_ENDPOINT,
				'values': [
					"""
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
					"""
				]
			},
			'getty': {
				'url': GETTY_ENDPOINT,
				'values': []
			}
		}
	},
	'timeliness': {
		'test_data': {
			'datahub': {
				'url': DATAHUB_ENDPOINT,
				'values': []

			},
			'getty': {
				'url': GETTY_ENDPOINT,
				'values': [
					"""
						PREFIX  dc: <http://purl.org/dc/elements/1.1/>
						PREFIX dct: <http://purl.org/dc/terms/>

						SELECT DISTINCT ?title ?created ?issued
						where {
						    ?s dct:title ?title .
						    ?s dct:created ?created .
						    ?s dct:issued ?issued .
						} LIMIT 1000
					""",
					"""
						PREFIX  dc: <http://purl.org/dc/elements/1.1/>
						PREFIX dct: <http://purl.org/dc/terms/>

						SELECT DISTINCT ?title ?issued ?modified
						where {
						    ?s dct:title ?title .
						    ?s dct:issued ?issued .
						    ?s dct:modified ?modified .
						} LIMIT 1000
					"""
				]
			},
			'opendata': {
				'url': OPENDATA_CZ,
				'values': [
					"""
						PREFIX  dc: <http://purl.org/dc/elements/1.1/>
						PREFIX dct: <http://purl.org/dc/terms/>

						SELECT DISTINCT ?title ?created ?issued
						where {
						    ?s dct:title ?title .
						    ?s dct:created ?created .
						    ?s dct:issued ?issued .
						} LIMIT 1000
					""",
					"""
						PREFIX  dc: <http://purl.org/dc/elements/1.1/>
						PREFIX dct: <http://purl.org/dc/terms/>

						SELECT DISTINCT ?title ?issued ?modified
						where {
						    ?s dct:title ?title .
						    ?s dct:issued ?issued .
						    ?s dct:modified ?modified .
						} LIMIT 1000
					"""
				]
			}
		}
	},
	'trustworthiness': {
		'test_data': {
			'datahub': {
				'url': DATAHUB_ENDPOINT,
				'values': [
					"""
						PREFIX  dc: <http://purl.org/dc/elements/1.1/>
						PREFIX dct: <http://purl.org/dc/terms/>

						SELECT DISTINCT ?title ?creator ?publisher
						where {
						   ?s dct:title ?title .
						   ?s dct:creator ?creator .
						   ?s dct:publisher ?publisher .
						} LIMIT 1000
					"""
				]
			},
			'getty': {
				'url': GETTY_ENDPOINT,
				'values': []
			},
			'opendata': {
				'url': OPENDATA_CZ,
				'values': [
					"""
						PREFIX  dc: <http://purl.org/dc/elements/1.1/>
						PREFIX dct: <http://purl.org/dc/terms/>

						SELECT DISTINCT ?title ?created ?issued
						where {
						    ?s dct:title ?title .
						    ?s dct:created ?created .
						    ?s dct:issued ?issued .
						} LIMIT 1000
					""",
					"""
						PREFIX  dc: <http://purl.org/dc/elements/1.1/>
						PREFIX dct: <http://purl.org/dc/terms/>

						SELECT DISTINCT ?title ?issued ?modified
						where {
						    ?s dct:title ?title .
						    ?s dct:issued ?issued .
						    ?s dct:modified ?modified .
						} LIMIT 1000
					"""
				]
			}
		}
	}
}
