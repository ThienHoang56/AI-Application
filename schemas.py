messages = [
    {
        "role": "user",
        "content": """ How can we fix the core business of this bad idea. This idea is bad due to not actually solving any pain points for users and it is just a copy paste of existing products. 
                    The idea: Vibe Spot. It is an app that allow people to look for coffee or restaurant that matches their "vibes". 
                    We don't even know what "vibe" can be handled?
                    Please return result in JSON format"""
    }
]

function_definition = [{
    'type':'function',
    'function':{
        'name':'get_properties',
        'description':'Get properties',
        'parameters':{
            'type' : 'object',
            'properties' : {
                'business' : {
                    'type' : 'string',
                    'description' : 'Business'
                },
                'description' : {
                    'type' : 'string',
                    'description' : 'Description of business'
                }
            },
            'required' : ['business']
        }
    }
}]
