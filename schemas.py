messages = [
    {
        "role": "user",
        "content": """ How can we fix the core business of this bad idea. 
                    This idea is bad due to not actually solving any pain points for users and it is just a copy paste of existing products. 
                    Product: Vibe Spot. 
                    Description: It is an app that allow people to look for coffee or restaurant that matches their "vibes". 
                    Problem: We don't even know what "vibe" can be handled? It is too vague
                    Please return result in JSON format"""
    }
]

function_definition = []

#Hàm để lấy thuộc tính product, business, description.
function_definition.append({
    'type':'function',
    'function':{
        'name':'clarify_business_idea',
        'description':'Clarify business idea',
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
})

#Đã làm rõ được ý tưởng, ta sẽ tìm các quán cà phê trong địa bàn đà nẵng
function_definition.append({
    'type' : 'function',
    'function': {
        'name':'get_location',
        'description':'Return list of coordinates of coffee shops in Da Nang near FPT University Da Nang',
        'parameters':{
            'type':'object',
            'properties':{
                'latitude' : {
                    'type' : 'number',
                    'description' : 'Latitude of coffee shops'
                },
                'longitude' : {
                    'type' : 'number',
                    'description' : 'Longitude of coffee shops'
                },
                'radius' : {
                    'type' : 'number',
                    'description' : 'Radius of coffee shops near FPTU Da Nang (Default = 10km)'
                }
            }
        }
    }
})
