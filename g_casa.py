import random

def generar_casa():
    return {
        "#" : random.randint(0, 7   ),
        "lt": random.randint(0, 20  ),
        "kw": random.randint(0 ,100 ),
    }
    
