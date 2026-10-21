from typing import TypedDict
from langgraph.graph import StateGraph,START,END


#state
class ComplimentSate(TypedDict):
    name:str
    quality:str
    interest:str
    compliment:str

class GraphState(TypedDict):
    name:str
    values:list[int]
    operation:str
    result:int
    message:str

#create node
def generate_compliment(state:ComplimentSate):
    name = state["name"]
    quality = state["quality"]
    interest = state["interest"]

    compliment = (
        f"{name},your :: {quality}"
        f"you interest :: {interest}"
    )

    return {"compliment": compliment}

def calculate(state:GraphState):
    values=state['values']
    operation = state["operation"]
    if operation == '+':
        answer = sum(values)
    elif operation == '*':
        answer = 1
        for value in values:
            answer *= value
    else:
        raise ValueError("operation must be + or *")
    
    return {
        "result" : answer,
        "message" : f"{state['name']},your operation is {answer}"
    }
        
# Keep these as separate graphs: each graph has its own state schema and task.
compliment_builder = StateGraph(ComplimentSate)
compliment_builder.add_node("generate_compliment", generate_compliment)
compliment_builder.add_edge(START, "generate_compliment")
compliment_builder.add_edge("generate_compliment", END)
compliment_agent = compliment_builder.compile()

calculation_builder = StateGraph(GraphState)
calculation_builder.add_node("calculate", calculate)
calculation_builder.add_edge(START, "calculate")
calculation_builder.add_edge("calculate", END)
calculation_graph = calculation_builder.compile()



name = input("Enter your name: ")
quality = input("Enter your best quality: ")
interest = input("Enter your interest: ")

compliment_result = compliment_agent.invoke({
    "name": name,
    "quality": quality,
    "interest": interest,
    "compliment": ""
})

calculation_result = calculation_graph.invoke({
    "name": "Jack Sparrow",
    "values": [1, 2, 3, 4],
    "operation": "*",
    "result": 0,
    "message": ""
})

print("\nYour personalized compliment:")
print(compliment_result["compliment"])


# result = compilement_agent.invoke({
#     "name" : "AKS",
#     "quality" : "hardworking",
#     "interest" : "python programming",
#     "compliment" : ""
# })

print("\nCalculation:")
print(calculation_result["message"])
# name = input("Enter your name: ")
# quality = input("Enter your best quality: ")
# interest = input("Enter your interest: ")

 
