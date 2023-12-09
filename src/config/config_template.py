config = {
    "openai": {
        "api_key": ""
    },
    "kafka": {
        "sasl.username": "",
        "sasl.password": "",
        "bootstrap.servers": "",
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms': 'PLAIN',
        'session.timeout.ms': 50000
    },
    "schema_registry": {
        "url" : "",
        "basic.auth.user.info" : "api_key:secret_key"
    },
    "sentiment_analysis":{
        'api_key':''
    }
}